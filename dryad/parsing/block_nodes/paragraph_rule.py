class ParagraphRule:
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
        yield doctree.Paragraph(inline_parser.parseInline(text))