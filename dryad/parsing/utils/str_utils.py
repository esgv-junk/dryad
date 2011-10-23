import itertools, re
from dryad.parsing.utils.re_utils import *

def is_char(s):
    return len(s) == 1

def make_indent(indent_level):
    return '    ' * indent_level

def reversed_dict(dict_):
    result = {}
    for k, v in dict_.items():
        result[v] = k
    return result

def multiple_replace(string, replace_dict):
    return re.sub(
        make_strings_re(replace_dict.keys()),
        lambda match_obj: replace_dict[match_obj.group(0)],
        string)
    
def escaped(string, descape_dict):
    return multiple_replace(string, reversed_dict(descape_dict))
    
def descaped(string, descape_dict):
    return multiple_replace(string, descape_dict)
