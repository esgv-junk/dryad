from pyforge.all import *

admonition_types = [
    'definition', 'theorem', 'paradox', 'statement', 'example', 'hypothesis',
    'paradox'
]

class MathAdmonitionBlock:
    def __init__(self, admonition_type, child_nodes):
        self.admonition_type = admonition_type
        self.child_nodes = child_nodes
    
def parse_math_admonition(block_name, inline_text, body_lines):
    from dryad.parsing import parse_blocks, parse_spans
    yield MathAdmonitionBlock(block_name, parse_blocks(body_lines))

admonition_type_re = make_strings_re(admonition_types)
    
block_parsers = [(admonition_type_re, parse_math_admonition)]
    