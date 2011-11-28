import pystache
from dryad.writer import str_nodes

invisible_block_template = """\
<span class="invisible">

{{{child_lines}}}

</span>"""


class InvisibleBlock:
    def write(self):
        context = {
            'child_lines': str_nodes(*self.child_nodes, sep='\n\n'),
        }
        
        return pystache.render(invisible_block_template, context)