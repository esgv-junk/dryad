import re
from pyforge.all import *
from dryad.markup.doctree import Node, Block
from dryad.markup.parser.java_iter import JavaIter
from dryad.markup.parser.utils import take_while

#                                 NODES

class List(Block):
    def __init__(self, items, marker_type):
        self.items = list(items)
        self.marker_type = marker_type

    doctree = ['items']

class ListItem(Node):
    def __init__(self, child_nodes, marker):
        self.child_nodes = list(child_nodes)
        self.marker = marker

    doctree = ['child_nodes']

#                               MARKERS

numeric_marker        = ur'(?:0|[1-9][0-9]*)[.)]'
auto_numeric_marker   = ur'\#[.)]'
unordered_dash_marker = ur'\-'
unordered_star_marker = ur'\*'

# not yet supported
#letter_marker = ur'[a-zA-Z][.)]'
#roman_marker  = ur'(?=.)M{0,4}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})[.)]'

#                               PARSING

@cache
def list_rule(marker):
    return ur'^(\s*)({0})(?: (.*))?$'.format(marker)

def list_action(marker):
    return lambda source_iter: list_parse_action(source_iter, marker)

def list_parse_action(source_iter, marker):
    items = []
    global_src_start = source_iter[0].line_number
    global_num_lines = 0

    while True:
        # check if we have one more item
        match_obj = re.match(list_rule(marker), source_iter[0])
        if not match_obj: break

        # HERE
        src_start = source_iter[0].line_number

        next(source_iter)

        # extract item attributes
        indent      = len(match_obj.group(1))
        item_marker = match_obj.group(2)[:-1]
        inline_text = match_obj.group(3) or ''
        item_lines = take_while(source_iter, lambda iter:
            get_indent(iter[0]) > indent or
            is_blank(iter[0])
        )
        num_spaces = indent + len(item_marker) + 2

        # HERE
        from dryad.utils.line import Line
        inline_text = Line(u' ' * num_spaces + inline_text)
        inline_text.line_number = src_start
        item_lines.insert(0, inline_text)
        #item_lines.insert(0, u' ' * num_spaces + inline_text)

        # parse item
        #items.append(parse_list_item(item_lines, item_marker))

        item = parse_list_item(item_lines, item_marker)
        item.src_start = src_start
        item.src_end = src_start + len(item_lines)
        global_num_lines += len(item_lines)
        items.append(item)

    return List(items, marker)

def parse_list_item(lines, marker):
    from dryad.markup.parser import parse_blocks
    return ListItem(parse_blocks(lines), marker)

#                               PLUGIN

BLOCK_RULES = [
    (list_rule(numeric_marker),        list_action(numeric_marker)),
    (list_rule(auto_numeric_marker),   list_action(auto_numeric_marker)),
    (list_rule(unordered_dash_marker), list_action(unordered_dash_marker)),
    (list_rule(unordered_star_marker), list_action(unordered_star_marker)),
]
