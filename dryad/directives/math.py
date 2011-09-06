from dryad.parsing import line_utils
from dryad.forge import *

from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

# ========================== MathBlock ==============================

class MathBlock(doctree.Block):
    pass

def parseMathBlock(inline, lines):
    return MathBlock(inline, lines)

def writeMathBlockHTML(node):
    with Tag('div', _class='math', nospace=True):
        writer.emitRaw('$$\n')

        # merge lines
        lines = '\n'.join(
            map(lambda l: escapeMath(l.indentedText()),
                [line_utils.Line(node.inline)]+node.lines))
        # write them out
        writer.emitRaw(lines)

        writer.emitRaw('\n$$\n')
        
    writer.emit('\n')

writer.nodeWriters[MathBlock, 'html'] = writeMathBlockHTML

# =========================== MathInline ============================

class MathInline(doctree.Inline):
    pass

def parseMathInline(text):
    return MathInline(text)

def writeMathInlineHTML(node):
    with Tag('span', _class='math'):
        writer.emitRaw('${0}$'.format(escapeMath(node.text)))

writer.nodeWriters[MathInline, 'html'] = writeMathInlineHTML