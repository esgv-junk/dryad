import re
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.line_utils import *
from dryad.parsing.utils.k_iter import * 


block_capturing_re = r'^\s*\[(.*?)\](.*)'
block_re           = capture_groups_removed(block_capturing_re)


class BlockRule:
    lookahead = 0
    
    @staticmethod
    def applies_to(source):
        # match name in brackets at the line start: '[name]...'
        return bool(re.match(block_re, source[0]))
                                        
        
    @staticmethod
    def parse(source):
                                        # extract block_name and inline_text
        match_obj = re.match(block_capturing_re, source[0])                      
        block_name, inline_text = match_obj.groups()

                                        # take all body_lines blank or more 
                                        # indented than the block itself
        start_indent = get_indent(source[0])
        eat(source, 1)
        body_lines = source.takewhile(
            lambda source: (
                get_indent(source[0]) > start_indent or 
                is_blank(source[0])
            ))

                                        # dedent them, strip blank body_lines 
        body_lines = dedented_by(       # at the end
            blank_lines_stripped_end(body_lines),
            start_indent
        )

                                        # and pass further
                                        # (depending on block type) 
        from dryad.doctree.block_nodes.block import Block
        yield Block(block_name, inline_text, body_lines)