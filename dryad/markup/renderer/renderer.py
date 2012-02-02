from os.path import join, exists, extsep, getmtime
from importlib import import_module
from pyforge.all import *
from jinja2 import BaseLoader, TemplateNotFound

class DryadRendererLoader(BaseLoader):
    @staticmethod
    def _get_source(template, renderer):
        path = join(
            renderer.__path__[0],
            'templates',
            template.replace('.', '/') + extsep + renderer.extension
        )

        if not exists(path):
            raise TemplateNotFound(template)

        mtime = getmtime(path)
        source = read_text_file(path)
        return source, path, lambda: mtime == getmtime(path)

    def get_source(self, environment, template):
        return self._get_source(template, get_renderer())

@cache
def get_view_module(node_class, renderer):
    node_module_local_path = drop_first_module(
        node_class.__module__,
        num_dropped=2
    )

    node_view_module_path = (
        renderer.__name__ +
        '.views.' +
        node_module_local_path
    )

    try:
        return import_module(node_view_module_path)
    except (ImportError, AttributeError):
        return None

@cache
def get_view(renderer):
    return jinja_env

@cache
def get_render_func(node_class, renderer):
    node_module_local_path = drop_first_module(
        node_class.__module__,
        num_dropped=2
    )

    try:
        template = get_view(renderer).get_template(node_module_local_path)
        return getattr(template.module, node_class.__name__)
    except (TemplateNotFound, AttributeError):
        if hasattr(renderer, 'fallbacks'):
            for fallback_renderer in renderer.fallbacks:
                render_func = get_render_func(fallback_renderer)
                if not (render_func is None):
                    return render_func

    return None

def render_node(node, renderer):
    node_class = node.__class__
    render_func = get_render_func(node_class, renderer)
    rendered_node = render_func(node)

    if rendered_node is None:
        raise NotImplementedError(
            "Renderer {0} doesn't dupport rendering of {1} nodes".format(
                renderer,
                node_class
            ))
    else:
        return rendered_node

def render_nodes(*nodes, sep='', renderer=None):
    if not (renderer is None):
        push_renderer(renderer)

    result = sep.join(render_node(node) for node in nodes)

    if not (renderer is None):
        pop_renderer()

    return result

jinja_env = jinja2.Environment(
    trim_blocks=False,
    autoescape=False,
    loader=DryadRendererLoader(),
    auto_reload=False
)

renderers_stack = []

def get_bundled_renderer_module(renderer_name):
    try:
        renderer_name = 'dryad.markup.renderer.' + renderer_name
        renderer_module = import_module(renderer_name)
    except ImportError:
        raise NotImplementedError('Renderer {0} not found'.format(renderer_name))

    return renderer_module

def push_renderer(renderer):
    if isinstance(renderer, str):
        renderer = get_bundled_renderer_module(renderer)

    jinja_env.cache.clear()
    renderers_stack.append(renderer)

def pop_renderer():
    jinja_env.cache.clear()
    renderers_stack.pop()

def get_renderer():
    return renderers_stack[-1]

jinja_env.filters['escape'] = \
    lambda string: multiple_replace(string, get_renderer().escapes)
jinja_env.filters['render'] = \
    lambda nodes, **kwargs: render_nodes(*nodes, **kwargs)
jinja_env.filters['hyphenate'] = hyphenate

render = render_nodes

push_renderer('html')
