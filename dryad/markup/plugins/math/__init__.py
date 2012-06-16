from dryad.markup.doctree import Span, Block

class MathBlock(Block):
    def __init__(self, body_lines):
        self.body_lines = list(body_lines)

class MathSpan(Span):
    def __init__(self, body_text):
        self.body_text = body_text

def parse_math_block(block_name, inline_text, body_lines):
    blocks = [block.strip() for block in '\n'.join(body_lines).split('\n\n')]
    nonempty_blocks = filter(bool, blocks)
    return [MathBlock(body_lines.split('\n')) for body_lines in nonempty_blocks]

def parse_math_span(span_name, body_text):
    return MathSpan(body_text)

BLOCK_PARSERS = [(u'^math$'    , parse_math_block)]
SPAN_PARSERS  = [(ur'^(math|\$)$', parse_math_span )]
