class Directive:
    lookahead = 0

    @staticmethod
    def isStartLine(source):
        # match name in brackets at the line start: '[name]'
        return bool(re.match(r'\[.*?\]', source[0].text))

    @staticmethod
    def parse(source):
        from .. import directives

        # extract dirType, inline
        dirType, inline = \
            re.match(r'^\[(.*?)\](.*)', source[0].text).groups()

        # take all lines more indented than the directive itself
        indent = source[0].indent
        next(source)
        lines = source.takewhile(lambda s: s[0].indent > indent or s[0].isBlank)

        # dedent them, strip blank lines at the end
        lines = map(lambda l: l.dedented(indent), lines)
        lines = line_utils.stripBlankLines(lines)

        # and pass further (depending on directive type)
        parser = directives.blockParsers[dirType]
        yield parser(inline, lines)