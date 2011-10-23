from dryad.parsing.utils.str_utils import *

class Block:
    def __init__(self, block_name, inline_text, body_lines):
        self.block_name = block_name
        self.inline_text = inline_text
        self.body_lines = list(body_lines)

    def pretty_format(self, indent_level=0):
        return (make_indent(indent_level) + 
                '<Block> [{block_name}] /{inline_text}/ {body_lines}'.format(
                    block_name =self.block_name,
                    inline_text=self.inline_text,
                    body_lines =self.body_lines))