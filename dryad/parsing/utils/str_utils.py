import itertools
import re

def is_char(s):
    return len(s) == 1

def reversed_dict(dict_):
    result = {}
    for k, v in dict_:
        result[v] = k

def multiple_replace(string, replace_dict):
    return re.sub(
        make_strings_re(replace_dict.keys()),
        lambda match_obj: replace_dict[match_obj.group(0)],
        string)
    
def escaped(string, escape_dict):
    return multiple_replace(string, escape_dict)
    
def descaped(string, escape_dict):
    return escaped(string, reversed_dict(escape_dict))