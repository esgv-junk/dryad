class Link:
    def __init__(self, href, body_text):
        self.href = href
        self.body_text = body_text

def parse_link(span_name, body_text):
    yield Link(span_name, body_text)
    
span_parsers = [(r'[a-z]+://.*', parse_link)]