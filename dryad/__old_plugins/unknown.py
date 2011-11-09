from .. forge import *
from dryad.parsing import line_utils

from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

class UnknownBlock(doctree.Block):
    def writeHTML(node):
        with Tag('div', _class='unknown', nospace=True):
            with Tag('pre'):
                for l in line_utils.dedentedByMin(node.allLines()):
                     writer.emit('{0}\n'.format(l.indentedText()))
        writer.emitRaw('\n')
    
    blockParsers = {'.*', 'verbatim'}
    writers = {'html': writeHTML}

class UnknownInline(doctree.Inline):
    def writeHTML(node):
        with Tag('span', _class='unknown'):
            with Tag('tt'):
                writer.emit(node.text)
           
    inlineParsers = {'.*', 'verbatim'}
    writers = {'html': writeHTML}   
