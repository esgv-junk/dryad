from pyforge.all import *
from dryad.markup.parser.k_iter import k_iter
from dryad.markup.doctree.walker import find, type_selector

math_include = """
\\renewcommand{\\Pr}{\\mathop{\\rm P}\\nolimits}
\\newcommand{\\ind}{\\mathop{\\rm I}\\nolimits}
\\newcommand{\\mean}{\\mathop{\\rm E}\\nolimits}
\\newcommand{\\var}{\\mathop{\\rm D}\\nolimits}
\\newcommand{\\cov}{\\mathop{\\rm cov}}

\\newcommand{\\rank}{\\mathop{\\rm rank}\\nolimits}
\\newcommand{\\tr}{\\mathop{\\rm tr}\\nolimits}
\\newcommand{\\dim}{\\mathop{\\rm dim}\\nolimits}
\\newcommand{\\ker}{\\mathop{\\rm ker}\\nolimits}
\\newcommand{\\im}{\\mathop{\\rm im}\\nolimits}

\\renewcommand{\\liminf}{\\mathop{\\overline{\lim}}}
\\renewcommand{\\limsup}{\\mathop{\\underline{\lim}}}
\\newcommand{\\to}{\\mathop\\longrightarrow}
\\newcommand{\\implies}{\\Rightarrow}
\\newcommand{\\intl}{\\int\\limits}
\\newcommand{\\iintl}{\\iint\\limits}
\\newcommand{\\iiintl}{\\iiint\\limits}
\\newcommand{\\d}{\\partial}
\\renewcommand{\\l}{\\left}
\\renewcommand{\\r}{\\right}

\\renewcommand{\\phi}{\\varphi}
\\newcommand{\\eps}{\\varepsilon}
\\renewcommand{\\emptyset}{\\varnothing}
\\renewcommand{\\mod}{\\,\\mathop{\\rm mod}\\,}
\\newcommand{\\const}{\\mathrm{const}}
"""

class MathBlock:
    def __init__(self, body_lines):
        self.body_lines = list(body_lines)
        
class MathSpan:
    def __init__(self, body_text):
        self.body_text = body_text
       
def parse_math_block(block_name, inline_text, body_lines):
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
    yield MathSpan(body_text)

def make_math_includes(root):
    # if math includes are not necessary, don't do them
    math_nodes = find(root, type_selector(MathBlock, MathSpan))
    if is_empty(math_nodes):
        return

    from dryad.markup.plugins.elements.invisible import InvisibleBlock
    # HACK: inserting into child_nodes[0], since it won't break TOC incorrect
    # behaviour
    root.child_nodes[0].child_nodes.insert(0, InvisibleBlock([ MathSpan(math_include) ]))

block_parsers        = [(r'math'   , parse_math_block)]
span_parsers         = [(r'math|\$', parse_math_span )]
after_parse_document = [make_math_includes]
