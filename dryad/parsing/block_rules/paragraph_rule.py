from dryad.parsing.utils.line_utils import *
from dryad.doctree.block_nodes.paragraph import Paragraph


class ParagraphRule:
    lookahead = 0

    @staticmethod
    def applies_to(source):
        return True                      # paragraph rule is 'last chance' rule

    @staticmethod
    def parse(source):
        from dryad.parsing import parse_blocks, parse_spans
        
        lines = source.takewhile(
            lambda source: not is_blank(source[0])
        )
        text = ' '.join(lines)
        yield Paragraph(parse_spans(text))