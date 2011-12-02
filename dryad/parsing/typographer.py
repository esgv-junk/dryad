import re
from pyforge.all import *


typographic_escapes = {
    '->' : '\u2192',
    '<-' : '\u2190',
    '<->': '\u2194',
    '--' : '\u2014',   # em dash
    ' - ': ' \u2014 ', # em dash (expreimental)
    '-'  : '\u2013'    # en dash
}

math_replaces = [
    (r'\\left\s*([(\[]|\\{)' , r'\1'),
    (r'\\right\s*([)\]]|\\})', r'\1'),
    (r'([(\[]|\\{)'          , r'\\left\1'),
    (r'([)\]]|\\})'          , r'\\right\1'),
]

def typograph_text(text):
    return multiple_replace(text, typographic_escapes)
    
def typograph_math(body_text):
    return multiple_replace_re(body_text, math_replaces)