from .. forge import *
from dryad.parsing import line_utils

from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

# ======================== UnknownBlock =============================

class UnknownBlock(doctree.Block):
    pass

def parseUnknownBlock(inline, lines):
    return UnknownBlock(inline, lines)

def writeUnknownBlockHTML(node):
    with Tag('div', _class='unknown', nospace=True):
        with Tag('pre'):
            for l in line_utils.dedentedByMin(node.allLines()):
                 writer.emit('{0}\n'.format(l.indentedText()))
    writer.emitRaw('\n')

writer.nodeWriters[UnknownBlock, 'html'] = writeUnknownBlockHTML

# ======================== UnknownInline ============================

class UnknownInline(doctree.Inline):
    pass

def parseUnknownInline(text):
    return UnknownInline(text)

def writeUnknownInlineHTML(node):
    with Tag('span', _class='unknown'):
        with Tag('tt'):
            writer.emit(node.text)

writer.nodeWriters[UnknownInline, 'html'] = writeUnknownInlineHTML