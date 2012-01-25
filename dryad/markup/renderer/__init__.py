import traceback
import pystache
from pyforge.all import *

render_template = pystache.render

def get_bundled_renderer_module(renderer_name):
    try:
        renderer_name = 'dryad.markup.renderer.' + renderer_name
        renderer_module = import_module(renderer_name)
    except ImportError:
        raise NotImplementedError('Renderer {0} not found'.format(renderer_name))

    return renderer_module

renderer_stack = []

def push_renderer(renderer):
    if isinstance(renderer, str):
        renderer = get_bundled_renderer_module(renderer)

    pystache.template.escape =\
        lambda string: multiple_replace(str(string), renderer.escapes)

    renderer_stack.append(renderer)

def pop_renderer():
    renderer_stack.pop()

def get_renderer():
    return renderer_stack[-1]

push_renderer('debug')

def render_node(node):
    node_class_name = node.__class__.__name__
    renderer_name = get_renderer().__name__

    # Turn something like 'dryad.markup.doctree.root'
    # into 'doctree.root'
    node_local_path = drop_first_module(node.__module__, num_dropped=2)

    # Eg. 'dryad.renderer.html.doctree.root'
    # (for the renderer 'dryad.renderer.html')
    node_writer_module_path = renderer_name + '.' + node_local_path

    try:
        # Import 'dryad.renderer.html.doctree.root'
        node_writer_module = import_module(node_writer_module_path)
        node_class = getattr(node_writer_module, node_class_name)
        node_class_write_func = node_class.write
    except (ImportError, AttributeError):
        raise NotImplementedError(
            "Renderer {0} doesn't implement rendering of {1}.{2} nodes.".format(
                renderer_name,
                node_local_path,
                node_class_name
            ))

    # Call 'dryad.renderer.html.doctree.root.Root.write(self=node)'
    return node_class_write_func(node)

def render_nodes(*nodes, sep='', renderer=None):
    if not (renderer is None):
        push_renderer(renderer)

    result = sep.join(render_node(node) for node in nodes)

    if not (renderer is None):
        pop_renderer()

    return result
