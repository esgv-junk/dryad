import itertools
from pyforge.all import *

supported_languages = [
    'code',                     # Do not highlight.
    'auto',                     # Automatically determine language. 
    'c++', 'cpp',               # C++         
    'python', 'python3'         # Python
]

class CodeBlock:
    def __init__(self, language, body_lines):
        self.language = language
        self.body_lines = list(body_lines)

class CodeSpan:
    def __init__(self, language, body_text):
        self.language = language
        self.body_text = body_text

def parse_code_block(block_name, inline_text, body_lines):
    body_lines = list(body_lines)
    min_indent = get_min_indent(body_lines)
    body_lines = dedented_by(body_lines, min_indent)
    body_lines = blank_lines_stripped(body_lines)
    
    yield CodeBlock(block_name, body_lines)

def parse_code_span(span_name, body_text):
    yield CodeSpan(span_name, body_text)

supported_languages_re = make_strings_re(supported_languages)
block_parsers          = [(supported_languages_re, parse_code_block)]
span_parsers           = [(supported_languages_re, parse_code_span )]

