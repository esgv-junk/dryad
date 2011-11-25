from dryad.writer import *
import pystache

math_admonition_template = """\
<math_admonition>
    <admonition_type> {{admonition_type}}
    <number> {{number}}
    <title> {{title_text}}
{{#body_lines}}
    {{{text}}}
{{/body_lines}}"""

class MathAdmonitionBlock:
    def write(self):
        context = {
            'admonition_type': self.admonition_type,
            'number'         : self.number,
            'title_text '    : str_nodes(*self.title_nodes), 
            'body_lines'     : pystache_lines(str_nodes(*self.child_nodes))
        }
        
        return pystache.render(math_admonition_template, context)