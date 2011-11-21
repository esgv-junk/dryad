import re
from pyforge.all import *
from dryad.doctree.emph import Emph


emph_escapes = {
    '\\\\': '\\',
   r'\*'   : '*' 
}

emph_capturing_re = r'\*({body_re})\*'.format(body_re=escaped_text_re) 

class EmphRule:
    rule_regexp = capture_groups_removed(emph_capturing_re)
    
    @staticmethod
    def parse(text):
        body_text = multiple_replace(
            re.match(emph_capturing_re, text).group(1),
            emph_escapes
        )
        
        from dryad.parsing import parse_blocks, parse_spans
        yield Emph(parse_spans(body_text))