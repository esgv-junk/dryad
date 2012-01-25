from dryad.markup.renderer import *
import pystache

math_admonition_template = """\
<math_admonition>
    <admonition_type> {{admonition_type}}
    <number> {{number}}
    <title> {{title_text}}
{{#child_lines}}
    {{{text}}}
{{/child_lines}}"""

class MathAdmonitionBlock:
    def write(self):
        context = {
            'admonition_type': self.admonition_type,
            'number'         : self.number,
            'title_text '    : render_nodes(*self.title_nodes),
            'child_lines'    : pystache_lines(render_nodes(*self.child_nodes))
        }
        
        return pystache.render(math_admonition_template, context)
