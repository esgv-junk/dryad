from dryad.markup.parser.utils import take_nonblank_lines
from dryad.markup.doctree import Block

#                                NODE

class Paragraph(Block):
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']

#                              PARSING

def paragraph_parse_rule(source_iter):
    return True

def paragraph_parse_action(source_iter):
    lines = take_nonblank_lines(source_iter)
    return parse_paragraph(u'paragraph', '', lines)

def parse_paragraph(block_name, inline_text, body_lines):
    text = ' '.join(line.strip() for line in body_lines)

    from dryad.markup.parser import parse_spans
    return Paragraph(parse_spans(text))

#                              PLUGIN

BLOCK_RULES   = [(paragraph_parse_rule, paragraph_parse_action)]
BLOCK_PARSERS = [(u'^paragraph$', parse_paragraph)]
