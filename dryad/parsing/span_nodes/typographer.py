from utils.str_re_utils import escaped

typographic_escapes = {
    '->' : '\u2192',
    '<-' : '\u2190',
    '<->': '\u2194',
    '--' : '\u2014', #em dash
    '-'  : '\u2013'  #en dash
}

def typographed(text):
    return escaped(text, typographic_escapes)

    