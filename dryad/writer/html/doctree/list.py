from dryad.writer import *
import pystache

list_template = """\
{{#is_ordered}}
<div class="list ordered">

<ol>

{{#items_lines}}
{{{text}}}
{{/items_lines}}
</ol>

</div>
{{/is_ordered}}
{{^is_ordered}}
<div class="list unordered">

<ul>

{{#items_lines}}
{{{text}}}
{{/items_lines}}
</ul>

</div>
{{/is_ordered}}

"""

class List:
    def write(self):
        context = {
            'is_ordered' : self.is_ordered,
            'items_lines': pystache_lines(
                str_nodes(*self.items) 
            )
        }
        
        return pystache.render(list_template, context)
    
item_template = """\
<li {{#has_value}}value="{{value}}" {{/has_value}}class="{{ord_class}}">

{{#child_lines}}
{{{text}}}
{{/child_lines}}
</li>

"""

class ListItem:
    def write(self):
        context = {
            'ord_class'  : (self.ord_number % 2) and 'odd' or 'even',
            'has_value'  : self.value is not None,
            'value'      : self.value,
            'child_lines': pystache_lines(
                str_nodes(*self.child_nodes)
            )
        }
        
        return pystache.render(item_template, context)