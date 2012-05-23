from pyforge.all import *

text_escapes = { 
    u'\\\\': u'\\',
    ur'\`' : u'`',
    ur'\*' : u'*'
}

class TextRule:
    rule_regexp = '.*?'
    
    @staticmethod
    def parse(text):
        from dryad.markup.parser import parse_span
        return parse_span(u'text', text)
    
span_rules = [TextRule]
