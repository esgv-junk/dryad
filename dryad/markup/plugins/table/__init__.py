from pyforge.all import *
from dryad.markup.doctree import Node, Block
from dryad.markup.parser.utils import take_while

# NODES

class Table(Block):
    def __init__(self, rows):
        self.rows = list(rows)

    doctree = ['rows']

class TableRow(Node):
    def __init__(self, cells):
        self.cells = list(cells)

    doctree = ['cells']

class TableCell(Node):
    def __init__(self, child_nodes, is_header_cell=False):
        self.child_nodes = list(child_nodes)
        self.is_header_cell = is_header_cell

    doctree = ['child_nodes']

# PARSING

table_parse_rule = ur'\s*({char}+( {char}+)+)'.format(char='[=\-]')

def table_parse_action(source_iter):
    # get outline (dedented) and indent
    outline = source_iter[0]
    outline_indent = get_indent(outline)
    dedented_outline = dedented_by(outline, outline_indent)
    eat(source_iter, 1)

    space_positions = [
        index
        for (index, char) in enumerate(dedented_outline)
        if char == ' '
    ]

    # check if there is header line
    header_line = None
    if source_iter[1] == outline:
        header_line = dedented_by(source_iter[0], outline_indent)
        eat(source_iter, 2)

    body_lines = take_while(
        source_iter,
        lambda iter: not (is_blank(iter[0]) or iter[0] == outline)
    )
    body_lines = dedented_by(body_lines, outline_indent)

    # the line in a table with 1 line is considered content, not header
    if not body_lines:
        body_lines = [header_line]
        header_line = None
    eat(source_iter, 1)

    # parse rows
    body_rows = (
        parse_table_row(body_line, space_positions)
        for body_line in body_lines
    )
    all_rows = body_rows
    if header_line:
        header_row = parse_table_row(header_line, space_positions, True)
        all_rows = chain([header_row], body_rows)

    return Table(all_rows)

def parse_table_row(line, split_positions, is_header_row=False):
    return TableRow(
        parse_table_cell(cell_text, is_header_row)
        for cell_text in split_string(split_positions, line)
    )

def parse_table_cell(cell_text, is_header_cell):
    from dryad.markup.parser import parse_spans
    return TableCell(parse_spans(cell_text), is_header_cell)

# PLUGIN

BLOCK_RULES = [(table_parse_rule, table_parse_action)]
