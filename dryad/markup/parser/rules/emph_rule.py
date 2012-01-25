import re
from pyforge.all import *
from dryad.markup.doctree.emph import Emph


emph_escapes = {
    '\\\\': '\\',
   r'\*'   : '*' 
}

class EmphRule:
    rule_regexp = '\*{body_re}\*'.format(body_re=backslash_escaped_text_re)
    
    @staticmethod
    def parse(text):
        body_text = multiple_replace(text[1:-1], emph_escapes)
        
        from dryad.markup.parser import parse_span
        return parse_span('emph', body_text)
    
span_rules = [EmphRule]
