class Strong:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']

def parse_strong(span_name, body_text):
    from dryad.markup.parser import parse_spans
    return Strong(parse_spans(body_text))

span_parsers = [(u'strong', parse_strong)]
