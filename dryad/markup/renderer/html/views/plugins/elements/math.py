from pyforge.all import *

math_escapes = {
    r'\$': r'\$',
    r'$' : r'\$'
}

def escape_math(string):
    return multiple_replace(string, math_escapes)
