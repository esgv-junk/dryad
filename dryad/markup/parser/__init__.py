import re, itertools
from pyforge.all import *
from dryad.markup.parser.k_iter import *

def load_plugins(module_names):
    lists_to_gather = get_objects_names(globals(), list)
    
    for module_name in module_names:
        module = import_module(module_name)
        
        for list_name in lists_to_gather: 
            gather_list(module, list_name, globals())

# callbacks

block_parsers         = []
span_parsers          = []
before_parse_document = []
after_parse_document  = []

@partial(works_with_line_list, (2, 'body_lines'))
def parse_block(block_name, inline_text, body_lines):
    for (block_name_re, parse_func) in block_parsers:
        
        block_name_re = make_exact(block_name_re)
        
        if re.match(block_name_re, block_name):
            return parse_func(block_name, inline_text, body_lines)

def parse_span(span_name, body_text):
    for (span_name_re, parse_func) in span_parsers:
        
        span_name_re = make_exact(span_name_re)
        
        if re.match(span_name_re, span_name):
            return parse_func(span_name, body_text)

# Parse functions have following flavors:
# 1. Parse blocks from text: parse(lines) 
# 2. Parse spans from text: parse(text)
# 3. Block rule callback: parse(source)
# 4. Span rule callback: parse(text)

block_rules = []
span_rules  = []

load_plugins([
    'dryad.markup.parser.rules.block_rule',
    'dryad.markup.parser.rules.list_rule',
    'dryad.markup.parser.rules.section_rule',
    'dryad.markup.parser.rules.table_rule',
    'dryad.markup.parser.rules.paragraph_rule',
    
    'dryad.markup.parser.rules.span_rule',
    'dryad.markup.parser.rules.strong_rule',
    'dryad.markup.parser.rules.emph_rule',
    'dryad.markup.parser.rules.text_rule'
])

from dryad.markup import plugins
load_plugins(plugins.plugin_list)

max_lookahead = max(map(lambda r: r.lookahead, block_rules))

@works_with_line_list
def parse_blocks(lines):
    source = k_iter(lines, lookahead=max_lookahead)
    next(source, None)                   # create context iterator and open it

    while True:
        while is_blank(source[0]):       # skip blank lines
            eat(source, 1)
            
        for rule in block_rules:         # check sequentially all parsing rules
            if rule.applies_to(source):
                for node in rule.parse(source):
                    yield node
                break
            
        if source.is_done:
            break
        
united_rules_re = (
    '(' + join_regexes(rule.rule_regexp for rule in span_rules) + ')'
) 

def parse_spans(text):
    for part in re.split(united_rules_re, text):
        if part == '':
            continue
        
        for rule in span_rules:
            if re.match(rule.rule_regexp, part):
                for node in rule.parse(part):
                    yield node
                break

# Escapes in span elements:
#    *           - within text, within strong/emph
#    `           - within text, within span
#    \           - within span, within strong/emph, within text
#    @, #, $, .. - no escapes 
#    []          - no escapes
#
# There are no escapes for span markers (like "@" and "[url]"). If you want to 
# write something like "\@``", write "@ ``" instead.
#
# When parser sees '\<x>' (<x> is a char) it does the following:
#     1) If '\<x>' is known escape _in the current context_, parser
#        replaces the escape sequence. 
#     2) Else, parser yields verbatim '\' and verbatim '<x>'.

from dryad.markup.doctree.root import Root

@works_with_line_list
def parse_document(lines):
    for callback in before_parse_document:
        callback()
        
    root = Root(parse_blocks(lines))
    
    for callback in after_parse_document:
        callback(root)
        
    return root

