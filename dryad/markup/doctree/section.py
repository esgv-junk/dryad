from pyforge.all import *
from dryad.markup.doctree import id_dispatcher

class Section:
    def __init__(self, section_level, title_nodes, child_nodes):
        self.section_level = section_level
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)
        
        self.section_id = id_dispatcher.dispatch_id(
            to_id(self.get_title_as_string())
        )
        
    def get_title_as_string(self):
        def get_span_text(span_node):
            if hasattr(span_node, 'body_text'):
                return span_node.body_text
            return ''

        return ''.join(
            get_span_text(title_node) 
            for title_node in self.title_nodes
        )

section_level = 0

def parse_section(block_name, inline_text, body_lines):
    #HACK: assigning section levels while parsing
    global section_level
    section_level += 1

    from dryad.markup.parser import parse_spans, parse_blocks
    
    title_nodes = parse_spans(inline_text)
    child_nodes = parse_blocks(body_lines)
    yield Section(section_level, title_nodes, child_nodes)

    section_level -= 1

block_parsers = [('section', parse_section)]
