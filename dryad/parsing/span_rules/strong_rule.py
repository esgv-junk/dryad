import re
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.str_utils import *
from dryad.doctree.span_nodes.strong import Strong


strong_escapes = {
    '\\\\': '\\',
   r'\*'   : '*' 
}

strong_capturing_re = r'\*\*({body_re})\*\*'.format(body_re=escaped_text_re) 

class StrongRule:
    rule_regexp = capture_groups_removed(strong_capturing_re)
    
    @staticmethod
    def parse(text):
        body_text = descaped(
            re.match(strong_capturing_re, text).group(1),
            strong_escapes
        )
        
        from dryad.parsing import parse_blocks, parse_spans
        yield Strong(parse_spans(body_text))