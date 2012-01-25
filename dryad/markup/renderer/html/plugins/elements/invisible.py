from dryad.markup.renderer import render_nodes, render_template

invisible_block_template = """\
<span class="invisible">

{{{child_lines}}}

</span>"""


class InvisibleBlock:
    def write(self):
        context = {
            'child_lines': render_nodes(*self.child_nodes, sep='\n\n'),
        }
        
        return render_template(invisible_block_template, context)
