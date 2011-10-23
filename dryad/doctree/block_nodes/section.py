from dryad.parsing.utils.str_utils import *
from dryad.doctree.block_nodes import pretty_format_blocks
from dryad.doctree.span_nodes import pretty_format_spans

heading_level = 1

class Section:
    def __init__(self, title_nodes, child_nodes):
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)

    def pretty_format(self, indent_level=0):
        return (make_indent(indent_level) + 
                '<Section>: {title_nodes}\n'.format(
                    title_nodes=pretty_format_spans(*self.title_nodes)) +
                pretty_format_blocks(*self.child_nodes, 
                                     indent_level=indent_level+1))

    def enterHTML(self):
        global heading_level
    
        writer.emitRaw('<div class="h{0}-outer">\n'.format(heading_level))
        with Tag('h{0}'.format(heading_level)):
            writer.walk(*node.titleNodes)
        writer.emitRaw('<div class="h{0}-inner">\n\n'.format(heading_level))
    
        heading_level += 1
    
    def exitHTML(self):
        global heading_level
        
        writer.emitRaw('</div>\n</div>\n\n')
        heading_level -= 1
        
    def write_HTML(self):
        pass
            
