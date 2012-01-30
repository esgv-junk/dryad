from itertools import chain

class InvisibleBlock:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']

def parse_invisible_block(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_blocks
    yield InvisibleBlock(parse_blocks(body_lines))

block_parsers = [('invisible', parse_invisible_block)]
