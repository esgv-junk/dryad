import re
from pyforge.all import *
from dryad.doctree.strong import Strong


strong_escapes = {
    '\\\\': '\\',
   r'\*'  : '*' 
}

strong_capturing_re = r'\*\*({body_re})\*\*'.format(body_re=escaped_text_re) 

class StrongRule:
    rule_regexp = capture_groups_removed(strong_capturing_re)
    
    @staticmethod
    def parse(text):
        body_text = multiple_replace(text[2:-2], strong_escapes)
        
        from dryad.parsing import parse_span
        return parse_span('strong', body_text)