from pyforge.all import *
from dryad.markup.parser.java_iter import JavaIter
from dryad.markup.parser.utils import skip_blank_lines
from dryad.markup.plugins.root import Root

#                          GENERIC MECHANISMS

def apply_parse_rules(rules, rule_arg, action_args):
    for rule, action in rules:
        current_arg = rule_arg
        if isinstance(rule, unicode):
            rule = regex_to_matcher(rule)
            if isinstance(rule_arg, JavaIter):
                current_arg = rule_arg[0]

        if rule(current_arg):
            return listify(action(*action_args))
    return []

#                          HIGH-LEVEL PARSERS

from dryad.markup.parser.config import \
    BLOCK_PARSERS, SPAN_PARSERS, BEFORE_PARSE_DOCUMENT, AFTER_PARSE_DOCUMENT

@partial(works_with_line_list, (2, 'body_lines'))
def parse_block(block_name, inline_text, body_lines):
    return apply_parse_rules(
        BLOCK_PARSERS,
        block_name,
        (block_name, inline_text, body_lines)
    )

def parse_span(span_name, body_text):
    return apply_parse_rules(SPAN_PARSERS, span_name, (span_name, body_text))

@works_with_line_list
def parse_document(lines):
    for callback in BEFORE_PARSE_DOCUMENT:
        callback()
    root = Root(parse_blocks(lines))
    for callback in AFTER_PARSE_DOCUMENT:
        callback(root)
    return root

#                    LOW-LEVEL BLOCK AND SPAN PARSERS

from dryad.markup.parser.config import \
    BLOCK_RULES, SPAN_RULES

@works_with_line_list
def parse_blocks(lines):
    stripped_lines = map(unicode.rstrip, lines)
    source_iter = JavaIter(stripped_lines, padding='')

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
        nodes = apply_parse_rules(SPAN_RULES, part, (part,))
        result.extend(nodes)
    return result
