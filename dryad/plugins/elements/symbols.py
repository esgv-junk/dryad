from pyforge.all import *

symbol_names = [
    'br'
]

class SymbolSpan:
    def __init__(self, symbol_name):
        self.symbol_name = symbol_name

def parse_symbol_span(span_name, inline_text):
    yield SymbolSpan(span_name)

symbol_name_re = make_strings_re(symbol_names)
span_parsers   = [(symbol_name_re, parse_symbol_span)]