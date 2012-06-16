from dryad.markup.doctree import Span
from urllib import quote

class Link(Span):
    def __init__(self, href, body_text):
        self.href = quote(href.encode('utf-8'), safe='/')
        self.body_text = body_text

def parse_link(span_name, body_text):
    if span_name == '@':
        span_name = body_text
    return Link(span_name, body_text)

SPAN_PARSERS = [(u'^(@|[a-z]+:.*)$', parse_link)]
