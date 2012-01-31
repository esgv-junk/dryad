from os.path import join, exists, extsep, getmtime
from importlib import import_module
import jinja2
from pyforge.all import *

def find_view_module(node_class, renderer):
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

class DryadRendererLoader(jinja2.BaseLoader):
    @staticmethod
    def _get_source(template, renderer):
        path = join(
            renderer.__path__[0],
            'templates',
            template.replace('.', '/') + extsep + renderer.extension
        )

        if not exists(path):
            raise jinja2.TemplateNotFound(template)

        mtime = getmtime(path)
        source = read_text_file(path)
        return source, path, lambda: mtime == getmtime(path)

    def get_source(self, environment, template):
        return self._get_source(template, get_renderer())

def find_template_render_func(node_class, renderer):
    node_module_local_path = drop_first_module(
        node_class.__module__,
        num_dropped=2
    )

    template = jinja_env.get_template(node_module_local_path)
    return getattr(template.module, node_class.__name__)

def render_node(node, node_class=None):
    renderer = get_renderer()
    if node_class is None:
        node_class = node.__class__

    view_module = find_view_module(node_class, renderer)
    render_template = find_template_render_func(node_class, renderer)

    if view_module is None:
        return render_template(node)
    else:
        return render_template(node, view_module)

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
