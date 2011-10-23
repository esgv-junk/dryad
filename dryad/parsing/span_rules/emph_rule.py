import re
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.str_utils import *
from dryad.doctree.span_nodes.emph import Emph

emph_escapes = {
    '\\\\': '\\',
   r'\*'   : '*' 
}

escaped_text_re = r'(?:[^\\]|\\.)+?'

emph_re_capturing = r'\*({body_re})\*'.format(
    body_re=escaped_text_re) 
    
class EmphRule:
    rule_regexp = capture_groups_removed(emph_re_capturing)
    
    @staticmethod
    def parse(text):
        body_text = descaped(
            re.match(emph_re_capturing, text).group(1),
            emph_escapes)
        
        from dryad.parsing import parse_blocks, parse_spans
        yield Emph(parse_spans(body_text))
        