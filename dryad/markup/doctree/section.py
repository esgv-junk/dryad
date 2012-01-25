from pyforge.all import *
from dryad.markup.doctree import id_dispatcher

class Section:
    def __init__(self, title_nodes, child_nodes):
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
    
def parse_section(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_spans, parse_blocks
    
    title_nodes = parse_spans(inline_text)
    child_nodes = parse_blocks(body_lines)
    yield Section(title_nodes, child_nodes)

block_parsers = [('section', parse_section)]
