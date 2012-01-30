class Emph:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    def __eq__(self, other):
        return isinstance(other, Emph) and self.child_nodes == other.child_nodes

    doctree = ['child_nodes']

def parse_emph(span_name, body_text):
    from dryad.markup.parser import parse_spans
    yield Emph(parse_spans(body_text))
    
span_parsers = [('emph', parse_emph)]
