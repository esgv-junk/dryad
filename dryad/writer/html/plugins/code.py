import pystache
import pygments, pygments.lexers, pygments.formatters
from dryad.writer import *


class CodeBlock:
    def write(self):
        body_text = '\n'.join(self.body_lines) or ' '
        
        if self.language == 'code':
            pygments_lexer = pygments.lexers.TextLexer()
        elif self.language == 'auto':
            pygments_lexer = pygments.lexers.guess_lexer(body_text)
        else:
            pygments_lexer = \
                pygments.lexers.get_lexer_by_name(self.language)
                
        pygments_formatter = pygments.formatters.HtmlFormatter(
            cssclass='code'
        )  
        
        body_html = pygments.highlight(
            body_text,
            pygments_lexer,
            pygments_formatter
        )
        
        return body_html
    
span_template = """\
<tt class="code">{{body_text}}</tt>"""

class CodeSpan:
    def write(self):
        context = {
            'body_text': self.body_text
        }
        
        return pystache.render(span_template, context)
    