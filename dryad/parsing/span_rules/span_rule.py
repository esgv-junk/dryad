import re
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.str_utils import *


span_markers = ['!', '@', '#', '$', '&']

span_escapes = {
    '\\\\': '\\',
   r'\`'  : '`'
}

span_capturing_re = r'({span_marker_re}|\[.*?\])?`({body_re})`'.format(
    span_marker_re=make_strings_re(span_markers),
    body_re=escaped_text_re
)


class SpanRule:
    rule_regexp = capture_groups_removed(span_capturing_re)
    
    @staticmethod
    def parse(text):
                                               # extract span_name and body_text
        span_name, body_text = re.match(span_capturing_re, text).groups()
        
        if span_name and span_name[:1] == '[': # strip brackets if there are
            span_name = span_name[1:-1] 
            
                                               # descape span escape sequences
        body_text = descaped(body_text, span_escapes)
        
                                               # pass further
        from dryad.doctree.span_nodes.span import Span
        yield Span(span_name, body_text)