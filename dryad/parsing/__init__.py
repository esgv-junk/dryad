import re, itertools

block_rules = [BlockRule, 
               ListRule, 
               SectionRule, 
               ParagraphRule]

max_lookahead = max(map(lambda r: r.lookahead, block_rules))

def parse_blocks(lines):
    source = k_iter(lines, max_lookahead)
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
#    *        - within text, within strong
#    `        - within text, within span
#    \        - within span, within strong, within text
#    @, #, .. - no escapes 
#    []       - no escapes
#
# There are no escapes for span markers (like "@" and "[url]"). If you want to 
# write something like "\@``", write "@ ``" instead.
#
# When parser sees '\<x>' (<x> is a char) it does the following:
#     1) If '\<x>' is known escape _in the current context_, parser
#        replaces the escape sequence. 
#     2) Else, parser yields verbatim '\' and verbatim '<x>'.

span_rules = [SpanRule,
              EmphRule,
              TextRule]

united_rules_re = '(' + join_regexes(
    *map(lambda rule: rule.rule_regex, span_rules)) + ')' 

def parse_spans(text):
    for part in re.split(united_rules_re, text):
        if part == '':
            continue
        
        for rule in span_rules:
            if re.match(rule.rule_regex, part):
                for node in rule.parse(part):
                    yield node
                continue