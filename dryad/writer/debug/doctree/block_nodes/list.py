from dryad.writer import *
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
                str_nodes(*self.items)
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
            'number': self.value,
            'child_lines': pystache_lines(
                str_nodes(*self.child_nodes)
            )
        }
        
        return pystache.render(item_template, context)