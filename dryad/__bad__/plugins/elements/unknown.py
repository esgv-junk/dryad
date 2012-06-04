class UnknownBlock:
    def __init__(self, block_name, inline_text, body_lines):
        self.block_name = block_name
        self.inline_text = inline_text
        self.body_lines = list(body_lines)

    def __eq__(self, other):
        return (
            isinstance(other, UnknownBlock) and
            self.block_name == other.block_name and
            self.inline_text == other.inline_text and
            self.body_lines == other.body_lines
        )

class UnknownSpan:
    def __init__(self, span_name, body_text):
        self.span_name = span_name
        self.body_text = body_text

    def __eq__(self, other):
        return (
            isinstance(other, UnknownSpan) and
            self.body_text == other.body_text
        )

def parse_unknown_block(block_name, inline_text, body_lines):
    yield UnknownBlock(block_name, inline_text, body_lines)

def parse_unknown_span(span_name, body_text):
    yield UnknownSpan(span_name, body_text)

block_parsers = [(u'.*', parse_unknown_block)]
block_parsers = [(u'.*', parse_unknown_block)]
span_parsers  = [(u'.*', parse_unknown_span )]
