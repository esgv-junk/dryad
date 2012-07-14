from pyforge.all import *

math_escapes = {
    u'<': u' < ',
    u'>': u' > '
}

def escape_math(string):
    return multiple_replace(string, math_escapes)
