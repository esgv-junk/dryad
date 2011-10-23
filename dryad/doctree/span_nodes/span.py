class Span:
    def __init__(self, span_name, body_text):
        self.span_name = span_name
        self.body_text = body_text

    def pretty_format(self):
        return '<Span> {span_name}/{body_text}/'.format(
            span_name=self.span_name,
            body_text=self.body_text)