from .. parsing import line_utils

from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

class CodeBlock:
    def __init__(self, name, inline, lines):
        self.language = inline

    def writeHTML(self):
        with Tag('div', _class='code', nospace=True):
            with Tag('pre'):
                for l in line_utils.dedentedByMin(self.lines):
                    writer.emit('{0}\n'.format(l.indentedText()))
        writer.emitRaw('\n')

    blockParsers = {'code':   'verbatim', 
                    'c++':    'verbatim',
                    'python': 'verbatim',
                    'sh':     'verbatim',
                    'make':   'verbatim'}
    
    writers = {'html': writeHTML}
    
    def pformat(self, indent = 0):
        return '{}Code ({}): {}'.format(
            '    ' * indent,
            self.language,
            self.lines)

class CodeSpan(doctree.Inline):
    def writeHTML(node):
        with Tag('span', _class='code'):
            with Tag('tt'):
                writer.emit(node.text)
                
    inlineParsers = {'code':   'verbatim', 
                     'c++':    'verbatim',
                     'python': 'verbatim',
                     'sh':     'verbatim',
                     'make':   'verbatim'}
    
    writers = {'html': writeHTML}
