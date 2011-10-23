from dryad.parsing import line_utils
from dryad.forge import *

from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

class MathBlock(doctree.Block):
    def writeHTML(node):
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
    
    blockParsers = {'math': 'verbatim'}
    writers = {'html': writeHTML}

# =========================== MathInline ============================

class MathInline(doctree.Inline):
    def writeHTML(node):
        with Tag('span', _class='math'):
            writer.emitRaw('${0}$'.format(escapeMath(node.text)))

    inlineParsers = {'math': 'verbatim',
                     '$': 'verbatim'}
    writers = {'html': writeHTML}