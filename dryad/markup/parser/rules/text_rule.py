from pyforge.all import *

text_escapes = { 
    '\\\\': '\\',
    r'\`' : '`',
    r'\*' : '*'
}

class TextRule:
    rule_regexp = '.*?'
    
    @staticmethod
    def parse(text):
        from dryad.markup.parser import parse_span
        return parse_span('text', text)
    
span_rules = [TextRule]
