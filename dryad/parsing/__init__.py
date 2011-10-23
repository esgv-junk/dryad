import re, itertools
from dryad.parsing.utils.re_utils import *
from dryad.parsing.utils.k_iter import *
from dryad.parsing.utils.line_utils import *

from dryad.parsing.block_rules import \
    block_rule, list_rule, section_rule, paragraph_rule

block_rules = [block_rule.    BlockRule, 
               list_rule.     OrderedListRule,
               list_rule.     UnorderedListRule, 
               section_rule.  SectionRule3,
               section_rule.  SectionRule2,
               paragraph_rule.ParagraphRule]

max_lookahead = max(map(lambda r: r.lookahead, block_rules))

def parse_blocks(lines):
    source = k_iter(lines, lookahead=max_lookahead)
    next(source, None)                  # create context iterator and open it

    while True:
        while is_blank(source[0]):        # skip blank lines
            next(source)
        for rule in block_rules:         # check sequentially all parsing rules
            if rule.applies_to(source):
                for node in rule.parse(source):
                    yield node
                break
            
# Escapes in span elements:
#    *           - within text, within strong
#    `           - within text, within span
#    \           - within span, within strong, within text
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

from dryad.parsing.span_rules import span_rule, emph_rule, text_rule 

span_rules = [span_rule.SpanRule,
              emph_rule.EmphRule,
              text_rule.TextRule]

united_rules_re = '(' + join_regexes(
    *map(lambda rule: rule.rule_regexp, span_rules)) + ')' 

def parse_spans(text):
    for part in re.split(united_rules_re, text):
        if part == '':
            continue
        
        for rule in span_rules:
            if re.match(rule.rule_regexp, part):
                for node in rule.parse(part):
                    yield node
                break