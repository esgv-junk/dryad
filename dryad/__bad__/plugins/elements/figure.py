from itertools import chain

class Figure:
    def __init__(self, caption_nodes, child_nodes):
        self.caption_nodes = list(caption_nodes)
        self.child_nodes = list(child_nodes)

    doctree = ['caption_nodes', 'child_nodes']

def parse_figure(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_blocks, parse_spans
    yield Figure(parse_spans(inline_text), parse_blocks(body_lines))

block_parsers = [(u'figure', parse_figure)]
