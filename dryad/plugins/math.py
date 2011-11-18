from dryad.parsing.k_iter import k_iter
from pyforge.iter_utils import *
from pyforge.line_utils import *

class MathBlock:
    def __init__(self, body_lines):
        self.body_lines = list(body_lines)
        
    @staticmethod
    def parse(block_name, inline_text, body_lines):
        if inline_text:                     # inline text goes into separate
            yield MathBlock([inline_text])  # block
            
        source = k_iter(body_lines, lookahead=0)
        next(source, None)

        while True:                         # yield blocks, divided by blank
            while is_blank(source[0]):      # lines
                eat(source, 1)
            
            body_lines = source.takewhile(
                lambda source: not is_blank(source[0])
            )
            yield MathBlock(body_lines)
                      
            if source.is_done: 
                break
        

class MathSpan:
    def __init__(self, body_text):
        self.body_text = body_text
    
    @staticmethod
    def parse(span_name, body_text):
        yield MathSpan(body_text)
