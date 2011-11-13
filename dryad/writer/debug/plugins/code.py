from dryad.writer import *
import pystache

block_template = """\
<code>
    <lang> {{language}}
{{#body_lines}}
    {{text}}
{{/body_lines}}"""

class CodeBlock:
    def write(self):
        context = {
            'language' : self.language,
            'body_lines' : pystache_lines(self.body_lines)
        }
        
        return pystache.render(block_template, context)

span_template = '<code lang="{{language}}">{{body_text}}</code>'

class CodeSpan:
    def write(self):
        context = {
            'lang': self.language,
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)