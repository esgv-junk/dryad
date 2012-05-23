import re
from pyforge.all import *
from dryad.markup.doctree.strong import Strong


strong_escapes = {
    u'\\\\': u'\\',
   ur'\*'  : u'*'
}

class StrongRule:
    rule_regexp = ur'\*\*{body_re}\*\*'.format(body_re=backslash_escaped_text_re)
    
    @staticmethod
    def parse(text):
        body_text = multiple_replace(text[2:-2], strong_escapes)
        
        from dryad.markup.parser import parse_span
        return parse_span(u'strong', body_text)
    
span_rules = [StrongRule]
