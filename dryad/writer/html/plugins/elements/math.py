import pystache
from pyforge.all import *

math_escapes = {
    r'\$': r'\$',
    r'$' : r'\$'
}

block_template = """\
<div class="math">
$$
{{body_lines}}
$$
</div>"""

span_template = '<span class="math">${{body_text}}$</span>'

class MathBlock:
    def write(self):        
        escaped_lines = (
            multiple_replace(line, math_escapes) 
            for line in self.body_lines
        )
        
        context = {
            'body_lines': '\n'.join(escaped_lines)
        }
        
        return pystache.render(block_template, context)

class MathSpan:
    def write(self):
        escaped_text = multiple_replace(self.body_text, math_escapes);
        
        context = {
            'body_text': escaped_text
        }
        
        return pystache.render(span_template, context)
    