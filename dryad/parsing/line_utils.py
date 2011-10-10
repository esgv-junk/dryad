import itertools

def indentation(line):
    result = 0
    while (result < len(self.text) and 
           line[result] == ' '):
        result += 1
    return result 

def is_blank(line):
    return Bool(line.strip())

def dedented_by(line, n):
    return line[min(n, indentation(line)):]

def strip_blank_lines(lines):
    lines = list(lines)
    if not lines:
        return lines

    last_line = len(lines)-1
    while last_line >= 0 and is_blank(lines[last_line]):
        last_line -= 1
    first_line = 0
    while first_line < len(lines) and is_blank(lines[first_line]):
        first_line += 1
        
    return lines[first_line:last_line+1]

def dedented_by_min_indentation(lines):
    lines = list(lines)
    min_indentation = min(
        itertools.chain(
            [999], 
            map(lambda l: indentation(l) if not is_blank(l) else 999, 
                lines)))
    return map(
        lambda l: dedented(l, min_indentation),
        lines)

#===============================================================================
#    #source = parsing.k_iter(lines, k = 0)
# 
#    #for l in source:
#    #    if not l.isBlank:
#    #        yield l
#    #    else:
#    #        blanks = 0
#    #        try:
#    #            while source[0].isBlank:
#    #                blanks += 1
#    #                next(source)
#    #            for i in range(blanks):
#    #                yield Line()
#    #        except:
#    #            pass
# 
#    # strip blank lines in the end
#===============================================================================
    
