from pyforge.all import *

#                              NODE

class Emph:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']

#                             PARSING

emph_parse_rule = ur'\*{0}\*'.format(backslash_escaped_text_re)

def emph_parse_action(text):
    return parse_emph(u'emph', text[1:-1])

def parse_emph(span_name, body_text):
    from dryad.markup.parser import parse_spans
    return Emph(parse_spans(body_text))

#                              PLUGIN

SPAN_RULES   = [(emph_parse_rule, emph_parse_action)]
SPAN_PARSERS = [(u'^emph$', parse_emph)]
