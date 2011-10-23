import re
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.line_utils import *

block_re_capturing = r'^\[(.*?)\](.*)'

block_re = capture_groups_removed(block_re_capturing)

class BlockRule:
    lookahead = 0
    
    @staticmethod
    def applies_to(source):
        # match name in brackets at the line start: '[name]'
        return bool(re.match(block_re, source[0]))

    @staticmethod
    def parse(source):
        # extract block_name and inline_text
        match_obj = re.match(block_re_capturing, source[0]) 
        block_name, inline_text = match_obj.groups()

        # take all body_lines blank or more indented than the block itself
        start_indent = get_indent(source[0])
        next(source)
        body_lines = source.takewhile(
            lambda source: (get_indent(source[0]) > start_indent) or 
                            is_blank(source[0]))

        # dedent them, strip blank body_lines at the end
        body_lines = dedented_by(
            blank_lines_stripped_end(body_lines),
            start_indent)

        # and pass further (depending on block type)
        parse_func = None # DISPATCH
        #for node in parse_func(block_name, inline_text, body_lines):
        #    yield node
        from dryad.doctree.block_nodes.block import Block
        yield Block(block_name, inline_text, body_lines)