from dryad.writer import *
import pystache

invisible_block_template = """\
<invisible>
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""

class InvisibleBlock:
    def write(self):
        context = {
            'child_lines': pystache_lines(str_nodes(*self.child_nodes))
        }
        
        return pystache.render(invisible_block_template, context)