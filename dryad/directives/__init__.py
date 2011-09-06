"""
Known directives
================

Code directives
---------------
    [code]
    [c++]
    [python]

Math directives
---------------
    [math]

    [definition]
    [example]
    [theorem]
        [proof]
    [lemma]
    [consequence]

Meta directives
---------------
    [include]
    [index]
    [meta]
    [todo]

Todo:
    code.py
        add highighting, line numbers, wrapping, copy button
    unknown.py
        add class to inlines
    math.py
        math preprocessing

    css addition?
    script addition?
    strongs customization.
"""

__all__ = []

import collections

from . import unknown
from . import code
from . import math
from . import math_blocks
from . import default
from . import image

blockParsers = collections.defaultdict(
    lambda: unknown.parseUnknownBlock,
    {
        'code': code.codeBlockParser('auto'),
        'c++': code.codeBlockParser('c++'),
        'python': code.codeBlockParser('python'),
        'sh': code.codeBlockParser('sh'),
        'make': code.codeBlockParser('make'),

        'math': math.parseMathBlock,

        'theorem': math_blocks.mathAdmonitionParser('theorem', 'theorem'),
        'definition': math_blocks.mathAdmonitionParser('definition', 'definition'),
        'example': math_blocks.mathAdmonitionParser('example'),
        'paradox': math_blocks.mathAdmonitionParser('paradox', 'theorem'),

        'image': image.parseImage
    }
)

inlineParsers = collections.defaultdict(
    lambda: unknown.parseUnknownInline,
    {
        '`': code.parseCodeInline,
        '[code]': code.parseCodeInline,
        '$': math.parseMathInline,
        '[math]': math.parseMathInline,
        None: default.parseDefault
    }
)

walkers = []

#writers = collections.defaultdict(
#    lambda: lambda node: None,
#    {
#        # HTML writers
#        (unknown.UnknownBlock, 'html'): unknown.writeUnknownBlockHTML,
#        (unknown.UnknownInline, 'html'): unknown.writeUnknownInlineHTML,
#
#        (code.CodeBlock, 'html'): code.writeCodeBlockHTML,
#        (code.CodeInline, 'html'): code.writeCodeInlineHTML,
#
#        (math.MathBlock, 'html'): math.writeMathBlockHTML,
#        (math.MathInline, 'html'): math.writeMathInlineHTML,
#
#        (math_blocks.MathAdmonition, 'html'):
#            (math_blocks.enterMathAdmonitionHTML,
#             math_blocks.exitMathAdmonitionHTML),
#
#        (image.Image, 'html'): image.writeImageHTML,
#
#        (default.Default, 'html'): default.writeDefaultHTML
#    }
#)