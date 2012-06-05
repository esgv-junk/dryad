from os.path import join, exists, getmtime, extsep
from importlib import import_module
from pyforge.all import *
from jinja2 import Environment, BaseLoader, TemplateNotFound

#
#                           JINJA ENVIRONMENT
#
class FileSystemLoader(BaseLoader):
    """
    Not like jinja2.FileSystemLoader. This class truly loads templates from
    file system using absolute path as template name.

    """

    def get_source(self, environment, template):
        path = template
        if not exists(path):
            raise TemplateNotFound(template)
        source = read_text_file(path)
        mtime = getmtime(path)
        return source, path, lambda: mtime == getmtime(path)

jinja_env = Environment(
    trim_blocks=False,
    loader=FileSystemLoader(),
    auto_reload=False
)

jinja_env.filters['escape'] = \
    lambda string: multiple_replace(string, get_renderer().ESCAPES)

jinja_env.filters['render'] = \
    lambda nodes, **kwargs: render(*nodes, **kwargs)

jinja_env.filters['hyphenate'] = hyphenate

#
#                        TEMPLATE SEARCH FUNCTIONS
#
def get_plugin_template_path(node_class, renderer):
    """
    Transforms "dryad.markup.plugins.text.Text" and renderer "html" into
    "dryad/markup/plugins/text/renderers/html/Text.html"

    """
    path = join(
        import_module(node_class.__module__).__path__[0],
        'renderers',
        renderer.__name__.rsplit('.', 1)[1],
        node_class.__name__ + extsep + renderer.TEMPLATE_EXTENSION)

    return path if exists(path) else None

def get_renderer_template_path(node_class, renderer):
    """
    Transforms "dryad.markup.plugins.text.Text" and renderer "html" into
    "dryad/renderer/html/templates/Text.html"

    """
    path = join(
        renderer.__path__[0],
        'templates',
        node_class.__name__ + extsep + renderer.TEMPLATE_EXTENSION)

    return path if exists(path) else None

@cache
def get_template_path(node_class, renderer):
    return (get_plugin_template_path(node_class, renderer) or
            get_renderer_template_path(node_class, renderer))


#
#                          VIEW SEARCH FUNCTIONS
#
def get_plugin_view_path(node_class, renderer):
    """
    Transforms "dryad.markup.plugins.text.Text" and renderer "html" into
    "dryad.markup.plugins.text.renderers"

    """
    return node_class.__module__ + '.renderers'

def get_renderer_view_path(node_class, renderer):
    return None

@cache
def get_view(node_class, renderer):
    view_path = (get_plugin_view_path(node_class, renderer) or
                 get_renderer_view_path(node_class, renderer))
    try:
        return import_module(view_path).__dict__
    except ImportError:
        return {}

@cache
def get_bundled_renderer_module(renderer_name):
    return import_module('dryad.markup.renderer.' + renderer_name)


#
#                           RENDERERS STACK
#
_renderers_stack = []

def push_renderer(renderer):
    if isinstance(renderer, str):
        renderer = get_bundled_renderer_module(renderer)
    jinja_env.cache.clear()
    _renderers_stack.append(renderer)

def pop_renderer():
    jinja_env.cache.clear()
    _renderers_stack.pop()

def get_renderer():
    return _renderers_stack[-1]


#
#                           RENDER FUNCTIONS
#
def render_node(node, renderer):
    path = get_template_path(node.__class__, renderer)
    if path is None:
        raise NotImplementedError(
            'Rendering of {0} nodes is not supported by {1} renderer'.format(
                node.__class__, renderer.__name__))

    template = jinja_env.get_template(path)
    view_env = get_view(node.__class__, renderer)
    view_env['node'] = node
    return template.render(view_env)

def render(*nodes, **kwargs):
    sep = kwargs.get('sep', '')
    renderer = kwargs.get('renderer', None)

    if renderer is not None:
        push_renderer(renderer)
    result = sep.join(render_node(node, get_renderer()) for node in nodes)
    if renderer is not None:
        pop_renderer()
    return result
