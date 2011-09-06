from .. parsing import line_utils

from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

# ========================= CodeBlock ===============================

class CodeBlock:
    def __init__(self, language, lines):
        self.language = language
        self.lines = list(lines)

    def pformat(self, indent = 0):
        return '{}Code ({}): {}'.format(
            '    ' * indent,
            self.language,
            self.lines)

def codeBlockParser(language):
    return lambda inline, lines: \
        CodeBlock(language, line_utils.dedentedByMin(lines))

def writeCodeBlockHTML(node):
    with Tag('div', _class='code', nospace=True):
        with Tag('pre'):
            for l in line_utils.dedentedByMin(node.lines):
                writer.emit('{0}\n'.format(l.indentedText()))
    writer.emitRaw('\n')

writer.nodeWriters[CodeBlock, 'html'] = writeCodeBlockHTML

# ======================== CodeInline ===============================

class CodeInline(doctree.Inline):
    pass

def parseCodeInline(text):
    return CodeInline(text)

def writeCodeInlineHTML(node):
    with Tag('span', _class='code'):
        with Tag('tt'):
            writer.emit(node.text)

writer.nodeWriters[CodeInline, 'html'] = writeCodeInlineHTML
