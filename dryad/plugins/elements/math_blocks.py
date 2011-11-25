from collections import defaultdict
from pyforge.all import *

admonition_types = [
    'theorem',
    'definition',
    'paradox',
    'hypothesis',
    'example',
    'statement',
    'proof',
    'remark',
    'consequence'
]

admonition_numbers = defaultdict(lambda: 1)

class MathAdmonitionBlock:
    def __init__(self, admonition_type, title_nodes, child_nodes):
        self.admonition_type = admonition_type
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)
        
        global admonition_numbers
        self.number = admonition_numbers[admonition_type]
        admonition_numbers[admonition_type] += 1
        
        if admonition_type != 'consequence':
            admonition_numbers['consequence'] = 1
    
def parse_math_admonition(block_name, inline_text, body_lines):
    from dryad.parsing import parse_blocks, parse_spans
    yield MathAdmonitionBlock(
        block_name, 
        parse_spans(inline_text.strip()), 
        parse_blocks(body_lines)
    )
    
def reset_state():
    admonition_numbers = defaultdict(lambda: 1)

admonition_type_re    = make_strings_re(admonition_types)
before_parse_document = [reset_state]
block_parsers         = [(admonition_type_re, parse_math_admonition)]
