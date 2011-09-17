import itertools
from .. parsing import line_utils

class Block:
    def __init__(self, name, inline, lines):
        self.name = name
        self.inline = inline
        self.lines = list(lines)

    def allLines(self):
        if self.inline:
            return itertools.chain(
                [line_utils.Line(self.inline)], 
                self.lines)
        else:
            return self.lines

    def pformat(self, indent = 0):
        return '{0}{1}: "{2}"/{3}'.format(
            '    ' * indent,
            type(self),
            self.inline,
            self.lines
        )

class Root:
    def __init__(self, children):
        self.children = list(children)

class Paragraph:
    def __init__(self, children):
        self.children = list(children)

    def pformat(self, indent = 0):
        return '{0}Paragraph: {1}'.format(
            '    ' * indent,
            ', '.join(map(lambda n: n.pformat(), self.children))
        )

class Section:
    def __init__(self, titleNodes, children):
        self.children = list(children)
        self.titleNodes = list(titleNodes)

    def pformat(self, indent = 0):
        return '{0}Section {1}\n'.format(
            '    ' * indent,
            ', '.join(map(lambda n: n.pformat(), self.titleNodes))
        ) + '\n'.join(map(lambda n: n.pformat(indent+1), self.children))

class ListItem:
    def __init__(self, value, children):
        self.value = value
        self.children = list(children)

    def pformat(self, indent = 0):
        return '{0}ListItem ({1})\n'.format(
            '    ' * indent,
            self.value,
        ) + '\n'.join(map(lambda n: n.pformat(indent+1), self.children))

class List:
    def __init__(self, ordered, children):
        self.ordered = ordered
        self.children = list(children)

    def pformat(self, indent = 0):
        return '{0}List ({1})\n'.format(
            '    ' * indent,
            'ordered' if self.ordered else 'unordered',
        ) + '\n'.join(map(lambda n: n.pformat(indent+1), self.children))
        