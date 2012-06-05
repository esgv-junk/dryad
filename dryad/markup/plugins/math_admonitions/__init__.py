from pyforge.all import *

admonition_types = [
    u'theorem',
    u'definition',
    u'paradox',
    u'hypothesis',
    u'example',
    u'statement',
    u'proof',
    u'remark',
    u'corollary',
    u'lemma'
]

class MathAdmonitionBlock:
    def __init__(self, admonition_type, title_nodes, child_nodes):
        self.admonition_type = admonition_type
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)

    doctree = ['title_nodes', 'child_nodes']

def parse_math_admonition(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_blocks, parse_spans
    return MathAdmonitionBlock(
        block_name,
        parse_spans(inline_text.strip()),
        parse_blocks(body_lines))

admonition_type_re = u'^' + make_strings_re(admonition_types) + u'$'

BLOCK_PARSERS = [(admonition_type_re, parse_math_admonition)]
