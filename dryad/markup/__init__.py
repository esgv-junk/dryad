__all__ = ['get_context', 'parse_document', 'render_document', 'render']

from dryad.markup.parser   import parse_document
from dryad.markup.renderer import render as render_nodes

_context = {}

def get_context():
    return _context

def render_document(document, renderer=None):
    return render_nodes(document, renderer=renderer)

def render(lines, renderer=None, context={}):
    global _context
    _context = context
    root = parse_document(lines)
    return render_nodes(root, renderer=renderer)
