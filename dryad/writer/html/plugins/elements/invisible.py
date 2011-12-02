from dryad.writer import str_nodes, render

invisible_block_template = """\
<span class="invisible">

{{{child_lines}}}

</span>"""


class InvisibleBlock:
    def write(self):
        context = {
            'child_lines': str_nodes(*self.child_nodes, sep='\n\n'),
        }
        
        return render(invisible_block_template, context)