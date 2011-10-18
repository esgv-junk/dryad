class ParagraphRule:
    lookahead = 0

    @staticmethod
    def applies_to(source):
        # paragraph rule is 'last chance' rule
        return True

    @staticmethod
    def parse(source):
        lines = source.takewhile(lambda s: not is_blank(s[0]))
        text = '\n'.join(lines)
        yield Paragraph(parse_spans(text))