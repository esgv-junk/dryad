class List:
    lookahead = 0;

    @staticmethod
    def caseO(source):
        return bool(re.match(
            r'^(?:{0}|\#)\.'.format('0|-?[1-9][0-9]*'),
            source[0].text))

    @staticmethod
    def caseU(source):
        return bool(re.match(
            r'^(?:[\-\*] )',
            source[0].text))

    @staticmethod
    def isStartLine(source):
        return List.caseO(source) or List.caseU(source)

    @staticmethod
    def parseListItems(lines):
        source = parsing.k_iter(lines, line_utils.Line(), k=0)
        next(source, None)

        while True:
            indent = source[0].indent

            if List.caseO(source):
                value, firstLine = re.match(
                    r'^({0}|\#)\.(.*)$'.format('0|-?[1-9][0-9]*'),
                    source[0].text).groups()
            else:
                value = None
                firstLine = re.match(
                    r'^(?:[\-\*] )(.*)',
                    source[0].text).group(1)

            next(source)
            value = int(value) if (value != '#' and value is not None) else None

            childLines = source.takewhile(
                lambda s: (s[0].indent > indent) or s[0].isBlank)
            allLines = itertools.chain([line_utils.Line(firstLine)],
                                       childLines)

            yield doctree.ListItem(value, parseBlocks(allLines))

    @staticmethod
    def parse(source):
        # take all lines more indented than the first line
        indent = source[0].indent

        def takeU(s):
            return s[0].indent > indent or \
                   s[0].isBlank or \
                   ((s[0].indent == indent) and List.caseU(s))

        def takeO(s):
            return s[0].indent > indent or \
                   s[0].isBlank or \
                   ((s[0].indent == indent) and List.caseO(s))

        ordered = List.caseO(source)
        lines = source.takewhile(takeO if ordered else takeU)

        yield doctree.List(ordered, List.parseListItems(lines))
