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
    (r'([(\[]|\\{)', r'\\left\1'),
    (r'([)\]]|\\})', r'\\right\1'),
]

math_replaces_2 = {
    '\\th'    : '\\mathrm{th}', 
    '\\rg'    : '\\mathrm{rg}',
    '\\tr'    : '\\mathrm{tr}',
    
    '\\to'    : '\\mathop\\longrightarrow',
    '\\intl'  : '\\intl\\limits',
    '\\iintl' : '\\iintl\\limits',
    '\\iiintl': '\\iiintl\\limits',
    '\\d'     : '\\partial',
    '\\bar'   : '\\overline',
    '\\eps'   : '\\varepsilon',
    '\\phi'   : '\\varphi'
}

def typograph_text(text):
    return multiple_replace(text, typographic_escapes)
    
def typograph_math(body_text):
    body_text = multiple_replace(body_text, math_replaces_2)
    return multiple_replace_re(body_text, math_replaces)