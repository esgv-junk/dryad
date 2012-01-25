from dryad.markup.renderer import render_nodes, pystache_lines, render_template

table_template = """\
<center>
<table>

{{{row_lines}}}

</table>
</center>"""

row_template = """\
<tr class="{{ord_class}}">

{{{cell_lines}}}

</tr>"""

cell_template = """\
<td>

{{{child_lines}}}

</td>"""

header_cell_template = """\
<th>

{{{child_lines}}}

</th>"""

class Table():
    def write(self):
        context = {
            'row_lines': render_nodes(*self.rows, sep='\n\n')
        }
        
        return render_template(table_template, context)
    
class TableRow():
    def write(self):
        context = {
            'cell_lines': render_nodes(*self.cells, sep='\n\n'),
            'ord_class' : (self.ord_number % 2) and 'odd' or 'even'
        }
        
        return render_template(row_template, context)
    
class TableCell():
    def write(self):
        context = {
            'child_lines': render_nodes(*self.child_nodes, sep='\n\n')
        }
        
        template = (
            header_cell_template 
            if self.is_header_cell
            else cell_template
        )
        
        return render_template(template, context)
