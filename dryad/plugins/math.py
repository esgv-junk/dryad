from pyforge.all import *
from dryad.parsing.k_iter import k_iter
from dryad.parsing.typographer import typograph_math

class MathBlock:
    def __init__(self, body_lines):
        self.body_lines = list(body_lines)
        
class MathSpan:
    def __init__(self, body_text):
        self.body_text = typograph_math(body_text)

def parse_math_block(block_name, inline_text, body_lines):
    if inline_text:                     # inline text goes into separate
        yield MathBlock([inline_text])  # block
        
    source = k_iter(body_lines, lookahead=0)
    next(source, None)

    while True:                         # yield blocks, divided by blank
        while is_blank(source[0]):      # lines
            eat(source, 1)
        
        body_lines = map(
            typograph_math,
            source.takewhile(lambda source: not is_blank(source[0]))
        )
        yield MathBlock(body_lines)
                  
        if source.is_done: 
            break
        
def parse_math_span(span_name, body_text):
    yield MathSpan(body_text)

block_parsers = [(r'math'   , parse_math_block)]
span_parsers  = [(r'math|\$', parse_math_span )]