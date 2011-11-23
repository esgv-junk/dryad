class Text:
    def __init__(self, body_text):
        self.body_text = body_text
        
        
def parse_text(span_name, body_text):
    body_text = typograph_text(body_text)
    yield Text(text)
        
span_parsers = [('text', parse_text)]