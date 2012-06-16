from pyforge.all import *
from dryad.markup.doctree import Span

#                              NODE
class Text(Span):
    def __init__(self, body_text):
        self.body_text = body_text


#                             PARSING

text_escapes = {u'``': u'`'}

def text_parse_action(text):
    body_text = multiple_replace(text, text_escapes)
    return parse_text(u'text', body_text)

def parse_text(span_name, body_text):
    return Text(body_text)


#                              PLUGIN

SPAN_RULES   = [(u'.*?', text_parse_action)]
SPAN_PARSERS = [(u'^text$', parse_text)]
