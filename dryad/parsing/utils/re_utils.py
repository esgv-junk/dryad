import itertools
import re

def make_strings_re(string_list):
    chars = map(re.escape, filter(is_char, string_list))
    strings = map(re.escape, itertools.filterfalse(is_char, string_list))
    
    if chars:
        chars_re = '[' + ''.join(chars) + ']'
    if strings:
        str_re = '|'.join(strings)

    return chars_re + ('|' if (chars and strings) else '') + str_re

def join_regexes(*regexes):
    enclosed_regexes = map(lambda r: '(?:{0})'.format(r), regexes) 
    return '|'.join(enclosed_regexes)

def capture_groups_removed(pattern):
    return re.sub(r'\((?=[^?])', r'\(\?:', pattern)

def regex_dispatch(dispatch_list, string):
    for (rule, result) in dispatch_list:
        if re.match(rule, string):
            return result