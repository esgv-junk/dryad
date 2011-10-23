import re
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.str_utils import *

span_markers = ['!', '@', '#', '$', '&']

escaped_text_re = r'(?:[^\\]|\\.)+?'
    
span_re_capturing = r'({span_marker_re}|\[.*?\])?`({body_re})`'.format(
    span_marker_re=make_strings_re(span_markers),
    body_re=escaped_text_re)

span_escapes = {
    '\\\\': '\\',
   r'\`'  : '`',
}

class SpanRule:
    rule_regexp = capture_groups_removed(span_re_capturing)
    
    @staticmethod
    def parse(text):
        # extract span_name and body_text
        span_name, body_text = \
            re.match(span_re_capturing, text).groups()
            
        # descape span escape sequences
        body_text = descaped(body_text, span_escapes)
            
        # pass further
        parse_func = None # DISPATCH
        #for node in parse_func(span_name, body_text):
        #    yield node
        from dryad.doctree.span_nodes.span import Span
        yield Span(span_name, body_text)