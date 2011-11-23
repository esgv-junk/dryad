import pystache
from dryad.writer import *

block_template = """\
<math>
{{#body_lines}}
    {{text}}
{{/body_lines}}
"""

class MathBlock:
    def write(self):
        context = {
            'body_lines': pystache_lines(self.body_lines)
        }
        
        return pystache.render(block_template, context)
    
    
span_template = '<math>{{body_text}}</math>'

class MathSpan:
    def write(self):
        context = {
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)