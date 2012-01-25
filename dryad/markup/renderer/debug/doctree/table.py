import pystache
from dryad.markup.renderer import *

table_template = """\
<table>
{{#row_lines}}
    {{{text}}}
{{/row_lines}}"""

table_row_template = """\
<table_row>
    <vert_span> {{vert_span}}
{{#cell_lines}}
    {{{text}}}
{{/cell_lines}}"""

table_cell_template = """\
<table_cell>
    <horiz_span> {{horiz_span}}
    <is_header_cell> {{is_header_cell}}
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""

class Table:
    def write(self):
        context = {
            'row_lines': pystache_lines(render_nodes(*self.rows)),
        }
        
        return pystache.render(table_template, context)
    
class TableRow:
    def write(self):
        context = {
            'cell_lines': pystache_lines(render_nodes(*self.cells)),
            'vert_span' : self.vert_span
        }
        
        return pystache.render(table_row_template, context)
    
class TableCell:
    def write(self):
        context = {
            'child_lines'   : pystache_lines(render_nodes(*self.child_nodes)),
            'horiz_span'    : self.horiz_span,
            'is_header_cell': self.is_header_cell
        }
        
        return pystache.render(table_cell_template, context)
