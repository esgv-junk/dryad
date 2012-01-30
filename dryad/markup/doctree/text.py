class Text:
    def __init__(self, body_text):
        self.body_text = body_text

    def __eq__(self, other):
        return isinstance(other, Text) and self.body_text == other.body_text

def parse_text(span_name, body_text):
    yield Text(body_text)
        
span_parsers = [('text', parse_text)]
