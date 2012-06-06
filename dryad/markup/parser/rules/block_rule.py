import re
from pyforge.all import *
from dryad.markup.parser.utils import take_while

#                              RULES

block_re           = ur'^\s*\[(.*?)\]((?:[^`].*)?)$'

def block_parsing_action(source_iter):
    match_obj = re.match(block_re, source_iter[0])
    block_name, inline_text = match_obj.groups()

    # take all body_lines blank or more indented than the block's first line
    start_indent = get_indent(source_iter[0])
    next(source_iter)
    body_lines = take_while(source_iter,
        lambda iter: (
            get_indent(iter[0]) > start_indent or
            is_blank(iter[0])
        ))

    # dedent taken lines, remove blank body_lines at the end
    body_lines = dedented_by(
        blank_lines_stripped_end(body_lines),
        start_indent
    )

    # pass further, depending on block type
    from dryad.markup.parser import parse_block
    return parse_block(block_name, inline_text, body_lines)

#                              PLUGIN

BLOCK_RULES = [(block_re, block_parsing_action)]
