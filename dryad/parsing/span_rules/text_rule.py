from dryad.parsing.utils.str_utils import *
from dryad.parsing.utils.k_iter import *
from dryad.parsing.typographer import typographed
from dryad.doctree.span_nodes.text import Text
 
 
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