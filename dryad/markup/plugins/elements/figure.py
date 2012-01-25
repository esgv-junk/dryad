from itertools import chain

class FigureBlock:
    def __init__(self, caption, child_nodes):
        self.caption = caption
        self.child_nodes = list(child_nodes)

def parse_figure_block(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_blocks
    yield FigureBlock(inline_text.strip(), parse_blocks(body_lines))

block_parsers = [('figure', parse_figure_block)]
