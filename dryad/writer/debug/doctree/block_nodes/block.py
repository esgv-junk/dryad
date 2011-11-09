from dryad.writer import *
import pystache

block_template = """\
<block>
    <block_name> {{block_name}}
    <inline_text> {{inline_text}}
{{#body_lines}}
    {{text}}
{{/body_lines}}"""

class Block:
    def write(self):
        context = {
            'block_name' : self.block_name,
            'inline_text': self.inline_text,
            'body_lines' : pystache_lines(self.body_lines)
        }
        
        return pystache.render(block_template, context)