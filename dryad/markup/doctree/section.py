from pyforge.all import *
from dryad.markup.doctree import id_dispatcher, type_selector, walk
from dryad.markup.renderer import render

class Section:
    def __init__(self, title_nodes, child_nodes):
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)
        
    def __eq__(self, other):
        return (
            isinstance(other, Section) and
            self.title_nodes == other.title_nodes and
            self.child_nodes == other.child_nodes
        )

    doctree = ['title_nodes', 'child_nodes']

def parse_section(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_spans, parse_blocks
    
    title_nodes = parse_spans(inline_text)
    child_nodes = parse_blocks(body_lines)
    yield Section(title_nodes, child_nodes)

def assign_section_levels_and_ids(root):
    section_level = 0

    def on_enter(node):
        nonlocal section_level
        section_level += 1
        node.section_level = section_level
        node.section_id = id_dispatcher.dispatch_id(
            to_id(render(*node.title_nodes, renderer='span_text'))
        )

    def on_exit(node):
        nonlocal section_level
        section_level -= 1

    eat(walk(root, on_enter, on_exit, type_selector(Section)))

block_parsers        = [('section', parse_section)]
after_parse_document = [assign_section_levels_and_ids]
