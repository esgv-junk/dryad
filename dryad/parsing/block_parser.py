import re, itertools

from . import line_utils
from .. import doctree
from .. import parsing
from .. parsing import inline_parser

class Paragraph:
    lookahead = 0

    @staticmethod
    def isStartLine(source):
        # paragraph rule is 'last chance' rule
        return True

    @staticmethod
    def parse(source):
        # text
        lines = source.takewhile(lambda s: not s[0].isBlank)
        text = ' '.join(map(lambda l: l.text, lines))

        # yield
        yield doctree.Paragraph(inline_parser.parseInline(text))

class Section:
    lookahead = 2

    @staticmethod
    def outlineRe(title):
        return r'^[=\-~]{{{0}}}$'.format(len(title.text))


    @staticmethod
    def case2(source):
        indMatch = source[0].indent == source[1].indent == 0
        title = source[0]
        return not source[0].isBlank and indMatch and re.match(Section.outlineRe(title), source[1].text)

    @staticmethod
    def case3(source):
        indMatch = source[0].indent == source[1].indent == \
                   source[2].indent == 0
        title = source[1]
        outlineRe = Section.outlineRe(title)
        return not source[0].isBlank and indMatch and re.match(outlineRe, source[0].text) and \
               re.match(outlineRe, source[2].text)

    @staticmethod
    def isStartLine(source):
        # match '======'-type pattern in the second line

        return Section.case2(source) or Section.case3(source)

    @staticmethod
    def parse(source):
        if Section.case2(source):
            title = source[0]
            headingChar = source[1].text[0]
            headingCase = 2
            parsing.eat(source, 2)
        else:
            title = source[1]
            headingChar = source[0].text[0]
            headingCase = 3
            parsing.eat(source, 3)

        titleNodes = inline_parser.parseInline(title.text)

        def take(s):
            nonlocal headingChar, headingCase
            if headingCase == 2:
                return not(Section.case2(s) and 
                    (s[1].text[0] == headingChar))
            else:
                return not(Section.case3(s) and
                    (s[0].text[0] == headingChar))

        lines = source.takewhile(take)

        # resulting node
        result = doctree.Section(titleNodes, list(parseBlocks(lines)))

        # yield
        yield result

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

parseRules = [Directive, List, Section, Paragraph]

lookahead = max(map(
    lambda r: r.lookahead,
    parseRules
))

def parseBlocks(lines):
    source = parsing.k_iter(lines, line_utils.Line(), lookahead)
    next(source, None)                  # create context iter and open it

    while True:
        while source[0].isBlank:        # skip blank lines
            next(source)

        for r in parseRules:            # iterate over all parse rules
            if r.isStartLine(source):
                for node in r.parse(source):
                    yield node
                break
