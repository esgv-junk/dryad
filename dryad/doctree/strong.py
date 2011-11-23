class Strong:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)
        
def parse_strong(span_name, body_text):
    from dryad.parsing import parse_spans
    yield Strong(parse_spans(body_text))
        
span_parsers = [('strong', parse_strong)]