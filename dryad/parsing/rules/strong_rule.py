import re
from pyforge.re_utils import *
from pyforge.str_utils import *
from dryad.doctree.strong import Strong


strong_escapes = {
    '\\\\': '\\',
   r'\*'   : '*' 
}

strong_capturing_re = r'\*\*({body_re})\*\*'.format(body_re=escaped_text_re) 

class StrongRule:
    rule_regexp = capture_groups_removed(strong_capturing_re)
    
    @staticmethod
    def parse(text):
        body_text = multiple_replace(
            re.match(strong_capturing_re, text).group(1),
            strong_escapes
        )
        
        from dryad.parsing import parse_blocks, parse_spans
        yield Strong(parse_spans(body_text))