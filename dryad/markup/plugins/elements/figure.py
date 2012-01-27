from itertools import chain

class Figure:
    def __init__(self, caption, child_nodes):
        self.caption = caption
        self.child_nodes = list(child_nodes)

def parse_figure(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_blocks
    yield Figure(inline_text.strip(), parse_blocks(body_lines))

block_parsers = [('figure', parse_figure)]
