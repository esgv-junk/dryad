class Link:
    def __init__(self, href, body_text):
        self.href = href
        self.body_text = body_text

def parse_link(span_name, body_text):
    if span_name == '@':
        span_name = body_text
    return Link(span_name, body_text)

SPAN_PARSERS = [(u'^(@|[a-z]+://.*)$', parse_link)]
