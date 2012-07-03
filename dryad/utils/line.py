from dryad.utils.meta import read_only_property, arg_decorator

# LINE AND LINE LIST

class Line(unicode):
    def __new__(cls, string, line_number=None):
        return unicode.__new__(cls, string)

    def __init__(self, string=u'', line_number=None):
        unicode.__init__(self, string)
        self.line_number = line_number

    def __repr__(self):
        return unicode(self) + u'//' + unicode(self.line_number)

    def lstrip(self, chars=None):
        return Line(unicode.lstrip(self), self.line_number)

    def rstrip(self, chars=None):
        return Line(unicode.rstrip(self), self.line_number)

    def strip(self, chars=None):
        return Line(unicode.strip(self), self.line_number)

    def __getslice__(self, i, j):
        return Line(unicode.__getslice__(self, i, j), self.line_number)

def line_list(string):
    lines = map(Line, string.splitlines())
    for number, line in enumerate(lines, 1):
        line.line_number = number
    return lines

@arg_decorator
def works_with_line_list(lines):
    return line_list(lines) if isinstance(lines, unicode) else lines

def is_blank(line):
    return not bool(line.strip())

# Working with indent

def get_indent(line):
    result = 0
    while (result < len(line) and
           line[result] == ' '):
        result += 1
    return result

"""
@partial(vectorize, (0, 'line'))
def dedented_by(line, amount):
    return line[min(amount, get_indent(line)):]

@partial(vectorize, (0, 'line'))
def indented_by(line, amount):
    return ' ' * amount + line

@partial(works_with_line_list, (0, 'lines'))
def get_min_indent(lines, blank_line_indent=sys.maxsize):

    def get_custom_indent(line):
        if not is_blank(line):
            return get_indent(line)
        else:
            return blank_line_indent

    indents = map(get_custom_indent, lines)
    return min(itertools.chain([sys.maxsize], indents))
"""
