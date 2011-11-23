from pyforge.all import *
from dryad.doctree.paragraph import Paragraph


class ParagraphRule:
    lookahead = 0

    @staticmethod
    def applies_to(source):
        return True                      # paragraph rule is 'last chance' rule

    @staticmethod
    def parse(source):
        from dryad.parsing import parse_blocks, parse_spans
        
        lines = source.takewhile(lambda source: not is_blank(source[0]))
        lines = (line.strip() for line in lines)
        text = ' '.join(lines)
        
        yield Paragraph(parse_spans(text))