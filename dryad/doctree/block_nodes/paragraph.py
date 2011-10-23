from dryad.parsing.utils.str_utils import *
from dryad.doctree.span_nodes import pretty_format_spans
from dryad.writer import emit, emit_raw

class Paragraph:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    def pretty_format(self, indent_level=0):
        return (make_indent(indent_level) + 
                '<Paragraph>: {child_nodes}'.format(
                    child_nodes=pretty_format_spans(*self.child_nodes)))
        
    def enterHTML(node):
        emit_raw('<p>')

    def exitHTML(node):
        emit_raw('''\
            </p>
            
            ''')
    
    writers = {
        'HTML': (enterHTML, exitHTML)
    }