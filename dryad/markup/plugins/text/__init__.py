class Text:
    def __init__(self, body_text):
        self.body_text = body_text

def parse_text(span_name, body_text):
    return Text(body_text)

span_parsers = [(u'text', parse_text)]
