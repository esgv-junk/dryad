import re
from pyforge.all import *

char_markers = ['!', '@', '#', '$', '&']

span_escapes = {
    '\\\\': '\\',
   r'\`'  : '`'
}

char_marker_re = make_strings_re(char_markers)
str_marker_re = r'\[.*?\]'
body_re = r'`({escaped_text_re})`'.format(
    escaped_text_re=escaped_text_re
)

span_capturing_re = \
    r'({str_marker}|{char_marker})?{body}|({str_marker})'.format(
        char_marker=char_marker_re,
        str_marker=str_marker_re,
        body=body_re
    )

class SpanRule:
    rule_regexp = capture_groups_removed(span_capturing_re)
    
    @staticmethod
    def parse(text):
                                               # extract span_name and body_text
        match_obj = re.match(span_capturing_re, text)
        span_name = match_obj.group(1) or match_obj.group(3) or ''
        body_text = match_obj.group(2) or ''
        
        if span_name and span_name[:1] == '[': # strip brackets if there are
            span_name = span_name[1:-1] 
            
                                               # descape span escape sequences
        body_text = multiple_replace(body_text, span_escapes)
        
                                               # pass further
        from dryad.parsing import parse_span
        return parse_span(span_name, body_text)
        