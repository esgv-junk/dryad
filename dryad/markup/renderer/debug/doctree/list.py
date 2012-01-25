from dryad.markup.renderer import *
import pystache

list_template = """\
<list>
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""

class List:
    def write(self):
        context = {
            'ordered': self.is_ordered,
            'child_lines': pystache_lines(
                render_nodes(*self.items)
            )
        }
        
        return pystache.render(list_template, context)
        
item_template = """\
<list_item>
    <number> {{item_num}}
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""
        
class ListItem:
    def write(self):
        context = {
            'item_num': self.value,
            'child_lines': pystache_lines(
                render_nodes(*self.child_nodes)
            )
        }
        
        return pystache.render(item_template, context)
