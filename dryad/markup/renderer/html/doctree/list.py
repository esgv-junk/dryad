from dryad.markup.renderer import render_nodes, render_template

ordered_list_template = """\
<ol>

{{{items_lines}}}

</ol>"""

unordered_list_template = """\
<ul>

{{{items_lines}}}

</ul>"""

item_template = """\
<li {{#has_value}}value="{{value}}" {{/has_value}}class="{{ord_class}}">

{{{child_lines}}}

</li>"""

class List:
    def write(self):
        context = {
            'items_lines': render_nodes(*self.items, sep='\n\n')
        }
        
        template = (
            ordered_list_template 
            if self.is_ordered 
            else unordered_list_template
        )
        
        return render_template(template, context)

class ListItem:
    def write(self):
        context = {
            'ord_class'  : (self.ord_number % 2) and 'odd' or 'even',
            'has_value'  : self.value is not None,
            'value'      : self.value,
            'child_lines': render_nodes(*self.child_nodes, sep='\n\n')
        }
        
        return render_template(item_template, context)
