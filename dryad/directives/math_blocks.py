from .. forge import *
import collections

from dryad import writer
from dryad.writer.html.tags import Tag

# ========================= MathAdmonition ==========================

class MathAdmonition:
    def __init__(self, admType, counter, nameNodes, children):
        self.admType = admType
        self.counter = counter
        self.nameNodes = list(nameNodes)
        self.children = list(children)

    def pformat(self, indent = 0):
        return '{0}{1} {2}\n'.format(
            '    ' * indent,
            self.admType,
            ', '.join(map(lambda n: n.pformat(), self.nameNodes))
        ) + '\n'.join(map(lambda n: n.pformat(indent+1), self.children))

def mathAdmonitionParser(admType, counter = None):
    def parseMathAdmonition(inline, lines):
        from .. parsing import block_parser, inline_parser

        nonlocal admType
        nonlocal counter

        return MathAdmonition(
            admType,
            counter,
            inline_parser.parseInline(inline),
            block_parser.parseBlocks(lines))

    return parseMathAdmonition

# TODO: redo this!

counters = collections.defaultdict(
    lambda: 0,
    {
        'definition': 1,
        'theorem': 1
    }
)

titles = collections.defaultdict(
    lambda: '',
    {
        'definition': 'Опр. {0}: ',
        'theorem': 'Теорема {0}: ',
        'example': 'Пример: ',
        'paradox': 'Парадокс {0}: '
    }
)

def enterMathAdmonitionHTML(node):
    from .. writer import html

    writer.emitRaw('<div class="{0}-outer">\n'.format(node.admType))

    with Tag('span', _class='{0}-title'.format(node.admType)):
        with Tag('strong'):
            writer.emit(
                titles[node.admType].format(
                    counters[node.counter]))

        writer.walk(*node.nameNodes)

    writer.emitRaw('\n<div class="{0}-inner">\n\n'.format(node.admType))

    if counters[node.counter]:
        counters[node.counter] += 1

def exitMathAdmonitionHTML(node):
    writer.emitRaw('</div>\n</div>\n\n')

writer.nodeWriters[MathAdmonition, 'html'] = \
    (enterMathAdmonitionHTML, exitMathAdmonitionHTML)