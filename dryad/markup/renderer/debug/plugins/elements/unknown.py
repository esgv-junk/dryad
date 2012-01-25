from dryad.markup.renderer import *
import pystache

block_template = """\
<block>
    <block_name> {{block_name}}
    <inline_text> {{inline_text}}
{{#body_lines}}
    {{text}}
{{/body_lines}}"""

class UnknownBlock:
    def write(self):
        context = {
            'block_name' : self.block_name,
            'inline_text': self.inline_text,
            'body_lines' : pystache_lines(self.body_lines)
        }
        
        return pystache.render(block_template, context)

span_template = '<span class="{{span_name}}">{{body_text}}</span>'

class UnknownSpan:
    def write(self):
        context = {
            'span_name': self.span_name,
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)
