import re
from pyforge.all import *

#                                ESCAPES

span_escapes = {u'``': u'`'}

#                                MARKERS

char_markers = u'!@#$&'
char_marker_re = '[' + re.escape(char_markers) + ']'
str_marker_re = ur'\[.*?\]'

#                                 RULE

span_re = \
    ur'({str_marker}|{char_marker})?`({body})`|({str_marker})'.format(
        char_marker=char_marker_re,
        str_marker=str_marker_re,
        body=backslash_escaped_text_re
    )


def span_parsing_action(text):
    match_obj = re.match(span_re, text)
    span_name = match_obj.group(1) or match_obj.group(3) or ''
    body_text = match_obj.group(2) or ''

    # strip brackets
    if span_name[:1] == '[':
        span_name = span_name[1:-1]

    from dryad.markup.parser import parse_span
    body_text = multiple_replace(body_text, span_escapes)
    return parse_span(span_name, body_text)

#                                PLUGIN

SPAN_RULES = [(span_re, span_parsing_action)]
