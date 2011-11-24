from dryad.parsing.typographer import typograph_text

class Text:
    def __init__(self, body_text):
        self.body_text = body_text
        
def parse_text(span_name, body_text):
    yield Text(typograph_text(body_text))
        
span_parsers = [('text', parse_text)]