import re
from pyforge.all import *

typographic_escapes = {
    '->' : '\u2192',
    '<-' : '\u2190',
    '<->': '\u2194',
    '--' : '\u2014',    # em dash
    '<<' : '\u00ab',    # left quote
    '>>' : '\u00bb'     # right quote
}

typographic_replaces = {
    (' - '     , ' \u2014 '),          # em dash (expreimental)
    (r'"(.*?)"', '\u00ab\\1\u00bb')
}

math_replaces = [
    (r'\\left\s*([(\[])' , r'\1'),
    (r'\\right\s*([)\]])', r'\1'),
    (r'\((.*?)\)'        , r'\\left( \1 \\right)'),
]

def typograph_text(text):
    text = multiple_replace(text, typographic_escapes)
    return multiple_replace_re(text, typographic_replaces)
    
def typograph_math(body_text):
    return multiple_replace_re(body_text, math_replaces)
