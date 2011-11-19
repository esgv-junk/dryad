import pystache
from pyforge.str_utils import *
from dryad.writer import *

block_template = """\
<div class="math">
$$
{{#body_lines}}
    {{text}}
{{/body_lines}}
$$
</div>
"""

math_escapes = {
    r'\$': r'\$',
    r'$' : r'\$'
}

class MathBlock:
    def write(self):        
        escaped_lines = map(
            lambda line: multiple_replace(line, math_escapes),
            self.body_lines
        )
        
        context = {
            'body_lines': pystache_lines(escaped_lines)
        }
        
        return pystache.render(block_template, context)

span_template = '<span class="math">${{body_text}}$</span>'

class MathSpan:
    def write(self):
        escaped_text = multiple_replace(self.body_text, math_escapes);
        
        context = {
            'body_text': escaped_text
        }
        
        return pystache.render(span_template, context)
    