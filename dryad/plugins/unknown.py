class UnknownBlock:
    def __init__(self, block_name, inline_text, body_lines):
        self.block_name = block_name
        self.inline_text = inline_text
        self.body_lines = list(body_lines)
        
    @staticmethod
    def parse(block_name, inline_text, body_lines):
        yield UnknownBlock(block_name, inline_text, body_lines)


class UnknownSpan:
    def __init__(self, span_name, body_text):
        self.span_name = span_name
        self.body_text = body_text
    
    @staticmethod
    def parse(span_name, body_text):
        yield UnknownSpan(span_name, body_text)
