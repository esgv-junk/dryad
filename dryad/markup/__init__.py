__all__ = ['parse_document', 'render_document', 'parse_and_render_document']

from dryad.markup.parser   import parse_document
from dryad.markup.renderer import render_nodes

def render_document(document, renderer=None):
    return render_nodes(document, renderer=renderer)

def parse_and_render_document(lines, renderer=None):
    root = parse_document(lines)
    return render_nodes(root, renderer=renderer)
