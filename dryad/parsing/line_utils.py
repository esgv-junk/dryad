import itertools

class Line:
    def __init__(self, text = '', indent = 0):
        self.text = text.expandtabs(4)

        self.indent = 0
        while self.indent < len(self.text) and self.text[self.indent] == ' ':
            self.indent += 1
        self.indent += indent

        self.text = self.text.strip(' \n')
        self.isBlank = self.text == ''

    def __repr__(self):
        return repr(self.text)+'({0})'.format(self.indent)

    def indentedText(self):
        return '{0}{1}'.format(' ' * self.indent, self.text)

    def dedented(self, n):
        l = Line(self.text, self.indent)
        l.indent -= n
        if l.indent < 0:
            l.indent = 0
        return l

def stripBlankLines(lines):
    #source = parsing.k_iter(lines, k = 0)

    #for l in source:
    #    if not l.isBlank:
    #        yield l
    #    else:
    #        blanks = 0
    #        try:
    #            while source[0].isBlank:
    #                blanks += 1
    #                next(source)
    #            for i in range(blanks):
    #                yield Line()
    #        except:
    #            pass

    # strip blank lines in the end
    lines = list(lines)
    if not lines:
        return lines

    end = len(lines)-1
    while end >= 0 and lines[end].isBlank:
        end -= 1

    start = 0
    while start < len(lines) and lines[start].isBlank:
        start += 1
        
    return lines[start:end+1]

def dedentedByMin(lines):
    lines = list(lines)
    minIndent = min(itertools.chain([999], map(lambda l: l.indent if not l.isBlank else 999, lines)))
    return map(
        lambda l: l.dedented(minIndent),
        lines
    )