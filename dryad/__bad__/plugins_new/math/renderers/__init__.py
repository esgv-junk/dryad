from pyforge.all import *

# '$' is not a math marker anymore, so we should escape it,
# even when rendering to LaTeX
math_escapes = {
    ur'\$': ur'\$',
    ur'$' : ur'\$'
}

def escape_math(string):
    return multiple_replace(string, math_escapes)
