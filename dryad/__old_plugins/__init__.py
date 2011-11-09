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