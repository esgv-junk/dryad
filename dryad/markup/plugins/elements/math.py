from pyforge.all import *
from dryad.markup.parser.k_iter import k_iter

math_include = """
\\newcommand{\\rank}{\\mathrm{rank}}
\\newcommand{\\tr}{\\mathrm{tr}}
\\newcommand{\\dim}{\\mathrm{dim}}
\\newcommand{\\ker}{\\mathrm{ker}}
\\newcommand{\\im}{\\mathrm{im}}

\\newcommand{\\to}{\\mathop\\longrightarrow}
\\newcommand{\\intl}{\\int\\limits}
\\newcommand{\\iintl}{\\iint\\limits}
\\newcommand{\\iiintl}{\\iiint\\limits}
\\newcommand{\\d}{\\partial}
\\newcommand{\\vbar}{\ \\big|\ }

\\renewcommand{\\phi}{\\varphi}
\\newcommand{\\eps}{\\varepsilon}
\\renewcommand{\\emptyset}{\\varnothing}
"""

"""\\renewcommand{\\bar}{\\overline}"""

math_include_done = False
 
def yield_math_includes():
    global math_include_done
    if math_include_done: 
        return []
    
    math_include_done = True
    
    from dryad.markup.plugins.elements.invisible import InvisibleBlock
    return [
        InvisibleBlock([ MathSpan(math_include) ])
    ]
    
def reset_state():
    global math_include_done
    math_include_done = False
    
before_parse_document = [reset_state]

class MathBlock:
    def __init__(self, body_lines):
        self.body_lines = list(body_lines)
        
class MathSpan:
    def __init__(self, body_text):
        self.body_text = body_text
       
def parse_math_block(block_name, inline_text, body_lines):
    for node in yield_math_includes():
        yield node
    
    if inline_text:                     # inline text goes into separate
        yield MathBlock([inline_text])  # block
        
    source = k_iter(body_lines, lookahead=0)
    next(source, None)

    while True:                         # yield blocks, divided by blank
        while is_blank(source[0]):      # lines
            eat(source, 1)
        
        body_lines = source.takewhile(lambda source: not is_blank(source[0]))
        yield MathBlock(body_lines)
                  
        if source.is_done: 
            break
        
def parse_math_span(span_name, body_text):
    for node in yield_math_includes():
        yield node
    
    yield MathSpan(body_text)

block_parsers = [(r'math'   , parse_math_block)]
span_parsers  = [(r'math|\$', parse_math_span )]
