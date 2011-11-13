import itertools
import pygments.lexers
from pyforge.line_utils import *
from pyforge.re_utils import *


pygments_languages = itertools.chain.from_iterable(
    aliases
    for (name, aliases, filetypes, mimetypes) in 
        pygments.lexers.get_all_lexers()  
)

language_re = make_exact(
    make_strings_re(itertools.chain(['auto', 'code'], pygments_languages))
)

class CodeBlock:
    def __init__(self, language, body_lines):
        self.language = language
        self.body_lines = list(body_lines)
        
    @staticmethod
    def parse(block_name, inline_text, body_lines):
        body_lines = list(body_lines) 
        body_lines = dedented_by(
            body_lines,
            get_min_indent(body_lines)
        )
        body_lines = blank_lines_stripped(body_lines)
        
        yield CodeBlock(block_name, body_lines)


class CodeSpan:
    def __init__(self, language, body_text):
        self.language = language
        self.body_text = body_text
    
    @staticmethod
    def parse(span_name, body_text):
        yield CodeSpan(span_name, body_text)
