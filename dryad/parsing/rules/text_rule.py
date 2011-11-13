from pyforge.str_utils import *
from dryad.parsing.typographer import typographed
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
        text = descaped(typographed(text), text_escapes)
        yield Text(text)