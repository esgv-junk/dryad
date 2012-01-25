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
    'consequence',
    'lemma'
]

admonition_numbers = NumberDispatcher()

class MathAdmonitionBlock:
    def __init__(self, admonition_type, title_nodes, child_nodes):
        self.admonition_type = admonition_type
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)
        self.number = admonition_numbers.dispatch_id(admonition_type)
        
        if admonition_type != 'consequence':
            admonition_numbers.reset_id('consequence')
    
def parse_math_admonition(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_blocks, parse_spans
    yield MathAdmonitionBlock(
        block_name, 
        parse_spans(inline_text.strip()), 
        parse_blocks(body_lines)
    )
    
def reset_admonition_numbers():
    admonition_numbers.clear()

admonition_type_re    = make_strings_re(admonition_types)

before_parse_document = [reset_admonition_numbers]
block_parsers         = [(admonition_type_re, parse_math_admonition)]
