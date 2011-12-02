from dryad.writer import render 
import pygments, pygments.lexers, pygments.formatters

span_template = """\
<tt class="code">{{body_text}}</tt>"""

class CodeBlock:
    def write(self):
        body_text = '\n'.join(self.body_lines) or ' '
        
        if self.language == 'code':         # just plain monotype-fonted code
            pygments_lexer = pygments.lexers.TextLexer()
            
        elif self.language == 'auto':       # automatically guess language
            pygments_lexer = pygments.lexers.guess_lexer(body_text)
            
        else:
            pygments_lexer = (              # language has been specified
                pygments.lexers.get_lexer_by_name(self.language)
            )
                
        pygments_formatter = pygments.formatters.HtmlFormatter(
            style='trac',
            cssclass='code'
        )  
        
        body_html = pygments.highlight(
            body_text,
            pygments_lexer,
            pygments_formatter
        )
        
        return body_html
    
class CodeSpan:
    def write(self):
        context = {
            'body_text': self.body_text
        }
        
        return render(span_template, context)
    