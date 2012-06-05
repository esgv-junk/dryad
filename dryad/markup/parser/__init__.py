from pyforge.all import *
from dryad.markup.parser.lookahead_iter import LookaheadIter
from dryad.markup.parser.utils import skip_blank_lines
from dryad.markup.plugins.root import Root

#                          GENERIC MECHANISMS

def apply_parse_rules(rules, rule_arg, action_args):
    for rule, action in rules:
        if isinstance(rule, unicode):
            rule = regex_to_matcher(rule)
            if isinstance(rule_arg, LookaheadIter):
                rule_arg = rule_arg[0]

        if rule(rule_arg):
            return listify(action(*action_args))
    return []

#                          HIGH-LEVEL PARSERS

BLOCK_PARSERS         = []
SPAN_PARSERS          = []
BEFORE_PARSE_DOCUMENT = []
AFTER_PARSE_DOCUMENT  = []

@partial(works_with_line_list, (2, 'body_lines'))
def parse_block(block_name, inline_text, body_lines):
    return apply_parse_rules(
        BLOCK_RULES,
        block_name,
        (block_name, inline_text, body_lines)
    )

def parse_span(span_name, body_text):
    return apply_parse_rules(SPAN_RULES, span_name, (span_name, body_text))

@works_with_line_list
def parse_document(lines):
    for callback in BEFORE_PARSE_DOCUMENT:
        callback()
    root = Root(parse_blocks(lines))
    for callback in AFTER_PARSE_DOCUMENT:
        callback(root)
    return root

#                    LOW-LEVEL BLOCK AND SPAN PARSERS

BLOCK_RULES = []
SPAN_RULES  = []

@works_with_line_list
def parse_blocks(lines):
    stripped_lines = map(unicode.strip, lines)
    source_iter = LookaheadIter(stripped_lines, padding='')

    result = []
    while True:
        skip_blank_lines(source_iter)
        if source_iter.is_done(): break
        nodes = apply_parse_rules(BLOCK_RULES, source_iter, (source_iter,))
        result.extend(nodes)
    return result

_split_re = make_split_re(zip(*SPAN_RULES)[0])

def parse_spans(text):
    result = []
    for part in re.split(_split_re, text):
        if not part: continue
        nodes = apply_parse_rules(SPAN_RULES, text, (text,))
        result.extend(nodes)
    return result
