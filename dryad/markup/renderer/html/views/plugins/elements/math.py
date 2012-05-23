from pyforge.all import *

math_escapes = {
    ur'\$': ur'\$',
    ur'$' : ur'\$'
}

def escape_math(string):
    return multiple_replace(string, math_escapes)
