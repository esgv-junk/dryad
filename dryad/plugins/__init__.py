import re
from pyforge.re_utils import *

from dryad.plugins.code import CodeBlock, CodeSpan, language_re
from dryad.plugins.image import ImageBlock
from dryad.plugins.default_span import set_default_span, parse_default_span
from dryad.plugins.unknown import UnknownBlock, UnknownSpan


block_regexes = [
    (language_re   , CodeBlock.parse   ),
    ('image'       , ImageBlock.parse  ),
    ('default_span', set_default_span  ),
    ('.*'          , UnknownBlock.parse)
]

span_regexes = [
    (language_re, CodeSpan.parse    ),
    (''         , parse_default_span),
    ('.*'       , UnknownSpan.parse )
]


def parse_block(block_name, inline_text, body_lines):
    for (block_name_re, parse_func) in block_regexes:
        
        block_name_re = make_exact(block_name_re)
        
        if re.match(block_name_re, block_name):
            for node in parse_func(block_name, inline_text, body_lines):
                yield node
            break

def parse_span(span_name, body_text):
    for (span_name_re, parse_func) in span_regexes:
        
        span_name_re = make_exact(span_name_re)
        
        if re.match(span_name_re, span_name):
            for node in parse_func(span_name, body_text):
                yield node
            break