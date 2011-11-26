from pyforge.all import *
from dryad.parsing.typographer import typograph_text
from dryad.doctree.text import Text
 
 
text_escapes = { 
    '\\\\': '\\',
    r'\`' : '`',
    r'\*' : '*'
}


class TextRule:
    rule_regexp = '.*?'
    
    @staticmethod
    def parse(text):
        from dryad.parsing import parse_span
        return parse_span('text', text)
    
span_rules = [TextRule]