from pyforge.all import *
from dryad.doctree.paragraph import Paragraph


class ParagraphRule:
    lookahead = 0

    @staticmethod
    def applies_to(source):
        return True                      # paragraph rule is 'last chance' rule

    @staticmethod
    def parse(source):
        body_lines = source.takewhile(lambda source: not is_blank(source[0]))
        
        from dryad.parsing import parse_block
        return parse_block('paragraph', '', body_lines)