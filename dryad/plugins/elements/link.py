class Link:
    def __init__(self, href, child_nodes):
        self.href = href
        self.child_nodes = child_nodes

def parse_link(span_name, body_text):
    from dryad.parsing import parse_spans
    yield Link(span_name, parse_spans(body_text))
    
span_parsers = [(r'[a-z]+://.*', parse_link)]