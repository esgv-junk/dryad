from itertools import chain

class InvisibleBlock:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

def parse_invisible_block(block_name, inline_text, body_lines):
    from dryad.parsing import parse_blocks
    all_lines = chain([inline_text], body_lines)
    yield InvisibleBlock(parse_blocks(all_lines))

block_parsers = [('invisible', parse_invisible_block)]
