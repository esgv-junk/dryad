import itertools
import sys


# Working with blank lines

def is_blank(line):
    return not bool(line.strip())

def blank_lines_stripped_start(lines):
    lines = list(lines)
    if not lines:
        return lines
    
    first_line = 0
    while first_line < len(lines) and is_blank(lines[first_line]):
        first_line += 1
    
    return lines[first_line:]

def blank_lines_stripped_end(lines):
    lines = list(lines)
    if not lines:
        return lines
    
    last_line = len(lines) - 1
    while last_line >= 0 and is_blank(lines[last_line]):
        last_line -= 1
        
    return lines[:last_line+1]

def blank_lines_stripped(lines):
    return blank_lines_stripped_start(
        blank_lines_stripped_end(lines)
    )


# Working with indent

def get_indent(line):
    result = 0
    while (result < len(line) and 
           line[result] == ' '):
        result += 1
    return result 

def dedented_by(line, amount):
    if isinstance(line, str):
        return line[min(amount, get_indent(line)):]
    else:
        return map(lambda l: dedented_by(l, amount),
                   line) 

def get_min_indent(lines, blank_line_indent=sys.maxsize):
    
    def get_custom_indent(line):
        if not is_blank(line):
            return get_indent(line)
        else:
            return blank_line_indent
        
    indents = map(lines, get_custom_indent(line))
    return min(itertools.chain([sys.maxsize], indents))