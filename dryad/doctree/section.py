from pyforge.all import *

taken_ids = {}

class Section:
    def __init__(self, title_nodes, child_nodes):
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)
        
        section_id = to_id(self.get_title_as_string())
        if section_id not in taken_ids:
            taken_ids[section_id] = 0
        else:
            taken_ids[section_id] += 1
            section_id += str(taken_ids[section_id])
        self.section_id = section_id
        
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
    from dryad.parsing import parse_spans, parse_blocks 
    
    title_nodes = parse_spans(inline_text)
    child_nodes = parse_blocks(body_lines)
    yield Section(title_nodes, child_nodes)

def reset_state():
    taken_ids = {}
    
block_parsers        = [('section', parse_section)]
after_parse_document = [reset_state]
        