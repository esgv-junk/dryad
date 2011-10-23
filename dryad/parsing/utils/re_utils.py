import itertools, re

# BUG: is duplicated in str_utils!
def is_char(s):
    return len(s) == 1

def make_strings_re(string_list):
    chars = map(re.escape, filter(is_char, string_list))
    strings = map(re.escape, itertools.filterfalse(is_char, string_list))
    
    char_class = ''.join(chars)
    chars_re = ('[' + char_class + ']'
        if char_class 
        else '')
    
    str_re = '|'.join(strings)
    
    return chars_re + ('|' if (chars_re and str_re) else '') + str_re

def join_regexes(*regexes):
    enclosed_regexes = map(lambda r: '(?:{0})'.format(r), regexes) 
    return '|'.join(enclosed_regexes)

# BUG: needs tweaking for named capture groups
def capture_groups_removed(pattern): 
    return re.sub(r'\((?=[^?])', r'(?:', pattern)

def regex_dispatch(dispatch_list, string):
    for (rule, result) in dispatch_list:
        if re.match(rule, string):
            return result