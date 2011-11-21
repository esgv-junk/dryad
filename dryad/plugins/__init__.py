import re
from pyforge.all import *

block_parsers = []
span_parsers  = []
before_parse_document = []
after_parse_document  = []

def load_plugins(*module_names):
    global block_parsers, span_parsers
    global before_parse_document, after_parse_document
    
    for module_name in module_names:
        module = __import__(module_name, fromlist=[module_name])
        
        lists_to_gather = [
            'block_parsers', 'span_parsers',
            'before_parse_document', 'after_parse_document'
        ]
         
        for list_name in lists_to_gather: 
            gather_list(module, list_name, globals())
        
load_plugins(
    'dryad.plugins.code', 
    'dryad.plugins.default_span', 
    'dryad.plugins.image', 
    'dryad.plugins.math_blocks', 
    'dryad.plugins.math', 
    'dryad.plugins.unknown'
)

def parse_block(block_name, inline_text, body_lines):
    for (block_name_re, parse_func) in block_parsers:
        
        block_name_re = make_exact(block_name_re)
        
        if re.match(block_name_re, block_name):
            for node in parse_func(block_name, inline_text, body_lines):
                yield node
            break

def parse_span(span_name, body_text):
    for (span_name_re, parse_func) in span_parsers:
        
        span_name_re = make_exact(span_name_re)
        
        if re.match(span_name_re, span_name):
            for node in parse_func(span_name, body_text):
                yield node
            break
        
        