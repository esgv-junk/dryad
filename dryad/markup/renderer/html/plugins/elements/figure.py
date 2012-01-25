from dryad.markup.renderer import render_nodes, render_template

figure_block_template = """\
<div class="figure">

{{{child_lines}}}

<p class="caption">{{caption}}</p>

</div>"""


class FigureBlock:
    def write(self):
        context = {
            'caption'    : self.caption,
            'child_lines': render_nodes(*self.child_nodes, sep='\n\n'),
        }
        
        return render_template(figure_block_template, context)
