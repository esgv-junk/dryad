from dryad.markup.doctree import Block, Span

# NODES

class UnknownBlock(Block):
    def __init__(self, block_name, inline_text, body_lines):
        self.block_name = block_name
        self.inline_text = inline_text
        self.body_lines = list(body_lines)

class UnknownSpan(Span):
    def __init__(self, span_name, body_text):
        self.span_name = span_name
        self.body_text = body_text

# PARSE

def parse_unknown_block(block_name, inline_text, body_lines):
    return UnknownBlock(block_name, inline_text, body_lines)

def parse_unknown_span(span_name, body_text):
    return UnknownSpan(span_name, body_text)

# PLUGIN

BLOCK_PARSERS = [(u'^.*$', parse_unknown_block)]
SPAN_PARSERS  = [(u'^.*$', parse_unknown_span )]
