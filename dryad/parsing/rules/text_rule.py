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
        text = multiple_replace(typograph_text(text), text_escapes)
        yield Text(text)