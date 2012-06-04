class MathBlock:
    def __init__(self, body_lines):
        self.body_lines = list(body_lines)

class MathSpan:
    def __init__(self, body_text):
        self.body_text = body_text

def parse_math_block(block_name, inline_text, body_lines):
    pass

def parse_math_span(span_name, body_text):
    return MathSpan(body_text)

block_parsers        = [(u'math'   , parse_math_block)]
span_parsers         = [(ur'math|\$', parse_math_span )]
after_parse_document = [make_math_includes]
