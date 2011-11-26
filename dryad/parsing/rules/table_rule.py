import re
from itertools import chain, islice
from pyforge.all import *
from dryad.doctree.table import Table, TableRow, TableCell
 
table_outline_re = r'\s*({char}+( {char}+)+)'.format(char='[=\-]')

class SimpleTableRule:
    lookahead = 2
    
    @staticmethod
    def applies_to(source):
        return bool(re.match(table_outline_re, source[0]))
    
    @staticmethod
    def parse(source):
        return parse_table(source)
        
def parse_table(source):
    outline = source[0]
    outline_indent = get_indent(outline)
    dedented_outline = dedented_by(outline, outline_indent)
    eat(source, 1)

    header_line = None    
    if source[1] == outline:
        header_line = dedented_by(source[0], outline_indent)
        eat(source, 2)
    
    space_positions = [
        index 
        for (index, char) in enumerate(dedented_outline)
        if char == ' '
    ]
    
    body_lines = source.takewhile(
        lambda source: not (
            is_blank(source[0]) or
            source[0] == outline
        )
    )
    body_lines = dedented_by(body_lines, outline_indent)
    body_lines = list(body_lines)
    eat(source, 1)
    
    
    body_rows = (
        parse_table_row(body_line, space_positions, False) 
        for body_line in body_lines
    )
    
    all_rows = body_rows
    if header_line is not None and header_line != '':
        header_row = parse_table_row(header_line, space_positions, True)
        all_rows = chain([header_row], body_rows)
    
    yield Table(all_rows)

def parse_table_row(line, split_positions, is_header_row):
    return TableRow(
        parse_table_cell(cell_text, is_header_row) 
        for cell_text in split_string(line, split_positions)
    )
        
def parse_table_cell(cell_text, is_header_cell):
    from dryad.parsing import parse_blocks
    return TableCell(parse_blocks(cell_text), is_header_cell)
        
block_rules = [SimpleTableRule]