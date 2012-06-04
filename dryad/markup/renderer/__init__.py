from os.path import join
from importlib import import_module
from pyforge.all import *
from jinja2 import Environment, FileSystemLoader

#
#                           JINJA ENVIRONMENT
#
jinja_env = Environment(
    trim_blocks=False,
    loader=FileSystemLoader("/"),
    auto_reload=False
)

jinja_env.filters['escape'] = \
    lambda string: multiple_replace(string, get_renderer().ESCAPES)

jinja_env.filters['render'] = \
    lambda nodes, **kwargs: render(*nodes, **kwargs)

jinja_env.filters['hyphenate'] = hyphenate

#
#                          SEARCH FUNCTIONS
#
def get_plugin_template_path(node_class, renderer):
    """
    Transforms "dryad.plugins.Text" and renderer "html" into
    "dryad/plugins/renderers/html/Text.html"

    """
    return join(
        node_class.__module__.__path__,
        'renderers',
        renderer.__name__,
        node_class.__name__ + '.' + renderer.TEMPLATE_EXTENSION)

def get_renderer_template_path(node_class, renderer):
    """
    Transforms "dryad.plugins.Text" and renderer "html" into
    "dryad/renderer/html/templates/Text.html"

    """
    return None

@cache
def get_template_path(node_class, renderer):
    return (get_plugin_template_path(node_class, renderer) or
            get_renderer_template_path(node_class, renderer))

@cache
def get_view(node_class, renderer):
    return {}

@cache
def get_bundled_renderer_module(renderer_name):
    return import_module('dryad.renerer.' + renderer_name)

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
