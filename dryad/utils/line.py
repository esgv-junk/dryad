from dryad.utils.meta import read_only_property, arg_decorator

class Line(unicode):
    def __new__(cls, string, _indent=None, _line_number=None):
        return unicode.__new__(cls, string)

    def __init__(self, string=u'', _indent=None, _line_number=None):
        unicode.__init__(self, string)

        self._line_number = -1 if _line_number is None else _line_number

        if _indent is None:
            self._indent = 0
            while self._indent < len(self) and self[self._indent] == ' ':
                self._indent += 1
            self._is_blank = not bool(unicode.strip(self))
        else:
            self._indent = _indent
            self._is_blank = (_indent != -1)

    def __repr__(self):
        return unicode(self) + u'//' + unicode(self._line_number)

    def lstrip(self, chars=None):
        return Line(unicode.lstrip(self), None, self._line_number)

    def rstrip(self, chars=None):
        return Line(unicode.rstrip(self), None, self._line_number)

    def strip(self, chars=None):
        return Line(unicode.strip(self), None, self._line_number)

    def __getslice__(self, i, j):
        return Line(unicode.__getslice__(self, i, j), None, self._line_number)

    indent      = read_only_property('_indent')
    line_number = read_only_property('_line_number')
    is_blank    = read_only_property('_is_blank')

def line_list(string):
    lines = map(Line, string.splitlines())
    for number, line in enumerate(lines, 1):
        line._line_number = number
    return lines

@arg_decorator
def works_with_line_list(lines):
    return line_list(lines) if isinstance(lines, unicode) else lines
