from pyforge.all import *
from dryad.markup.doctree import Span

#                              NODE

class Strong(Span):
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']

#                             PARSING

strong_parse_rule = ur'\*\*{0}\*\*'.format(backslash_escaped_text_re)

def strong_parse_action(text):
    return parse_strong(u'emph', text[2:-2])

def parse_strong(span_name, body_text):
    from dryad.markup.parser import parse_spans
    return Strong(parse_spans(body_text))

#                              PLUGIN

SPAN_RULES   = [(strong_parse_rule, strong_parse_action)]
SPAN_PARSERS = [(u'^strong$', parse_strong)]


