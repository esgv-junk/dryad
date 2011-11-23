class Text:
    def __init__(self, text):
        self.text = text
        
def parse_text(span_name, body_text):
    pass
        
span_parsers = [('text', parse_text)]