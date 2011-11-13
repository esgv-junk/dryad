from dryad.plugins.code import CodeBlock, CodeSpan, language_re
from dryad.plugins.unknown import UnknownBlock, UnknownSpan

block_regexes = [
    (language_re, CodeBlock.parse),
    ('.*', UnknownBlock.parse)
]

span_regexes = [
    (language_re, CodeSpan.parse),
    ('.*', CodeSpan.parse),
    ('.*', UnknownSpan.parse)
]