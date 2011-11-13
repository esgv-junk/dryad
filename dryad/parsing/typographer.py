from pyforge.str_utils import *

typographic_escapes = {
    '->' : '\u2192',
    '<-' : '\u2190',
    '<->': '\u2194',
    '--' : '\u2014',   # em dash
    ' - ': ' \u2014 ', # em dash (expreimental)
    '-'  : '\u2013'    # en dash
}

def typographed(text):
    return descaped(text, typographic_escapes)

    