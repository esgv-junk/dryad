class Strike:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)
        
def parse_strike(span_name, body_text):
    from dryad.markup.parser import parse_spans
    yield Strike(parse_spans(body_text))
    
span_parsers = [('strike', parse_strike)]
