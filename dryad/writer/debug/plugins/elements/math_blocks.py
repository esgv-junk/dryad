from dryad.writer import *
import pystache

math_admonition_template = """\
<math_admonition>
    <admonition_type> {{admonition_type}}
{{#body_lines}}
    {{{text}}}
{{/body_lines}}"""

class MathAdmonitionBlock:
    def write(self):
        context = {
            'admonition_type': self.admonition_type, 
            'body_lines'     : pystache_lines(str_nodes(*self.child_nodes))
        }
        
        return pystache.render(math_admonition_template, context)