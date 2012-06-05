from pyforge.all import *

#                             PARSE UTILITIES

def take_while(source_iter, pred):
    result = []
    while not source_iter.is_done() and pred(source_iter):
        result.append(next(source_iter))
    return result

def skip_blank_lines(source_iter):
    take_while(source_iter, lambda iter: is_blank(iter[0]))

def take_nonblank_lines(source_iter):
    return take_while(source_iter, lambda iter: not is_blank(iter[0]))

