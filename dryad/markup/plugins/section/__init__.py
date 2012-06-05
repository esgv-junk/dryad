import re
from urllib import quote
from pyforge.all import *
from dryad.markup.doctree import type_selector, walk
from dryad.markup.parser.utils import take_while
from dryad.markup.renderer import render

#                                NODE

class Section:
    def __init__(self, title_nodes, child_nodes):
        self.title_nodes = list(title_nodes)
        self.child_nodes = list(child_nodes)

    doctree = ['title_nodes', 'child_nodes']

#                           GENERAL PARSING

outline_chars = u'=-~'

def title_matches_outline(title, outline, chars):
    indents_ok = (get_indent(title) == get_indent(outline) == 0)
    outline_re = u"^{char}{{{min_repeats},{min_repeats}}}$".format(
        char=make_chars_re(chars),
        min_repeats=len(title))
    return indents_ok and not is_blank(title) and re.match(outline_re, outline)

def parse_section(block_name, inline_text, body_lines):
    from dryad.markup.parser import parse_spans, parse_blocks

    title_nodes = parse_spans(inline_text)
    child_nodes = parse_blocks(body_lines)
    return Section(title_nodes, child_nodes)


#                        PARSING SINGLE OUTLINE

def section_rule_2(source_iter, chars=outline_chars):
    return title_matches_outline(source_iter[0], source_iter[1], chars)

def section_parse_action_2(source_iter):
    title = source_iter[0]
    current_char = source_iter[1][0]
    eat(source_iter, 2)

    body_lines = take_while(source_iter, lambda iter: not(
        section_rule_2(iter, current_char) and
        iter[1] != iter[-1]))

    return parse_section(u'section', title, body_lines)

#                        PARSING DOUBLE OUTLINE

def section_rule_3(source_iter, chars=outline_chars):
    return (title_matches_outline(source_iter[1], source_iter[0], chars) and
            source_iter[2] == source_iter[0])

def section_parse_action_3(source_iter):
    title = source_iter[1]
    current_char = source_iter[1][0]
    eat(source_iter, 3)

    body_lines = take_while(source_iter, lambda iter: not(
        section_rule_3(iter, current_char)))

    return parse_section(u'section', title, body_lines)

#                              PLUGINS

def to_url(anchor):
    return quote(anchor.replace(' ', '_').encode('utf-8'), safe='')

def assign_section_levels_and_anchors(root):
    section_level = [0]

    def assign_level_and_anchor(node, section_level):
        section_level[0] += 1
        node.section_level = section_level[0]
        node.section_anchor = \
            to_url(render(*node.title_nodes, renderer='span_text'))

    def decrease_level(node, section_level):
        section_level[0] -= 1

    on_enter = lambda node: assign_level_and_anchor(node, section_level)
    on_exit  = lambda node: decrease_level(node, section_level)
    walk(root, on_enter, on_exit, type_selector(Section))


BLOCK_RULES = [(section_rule_2, section_parse_action_2),
               (section_rule_3, section_parse_action_3)]

BLOCK_PARSERS        = [(u'^section$', parse_section)]
AFTER_PARSE_DOCUMENT = [assign_section_levels_and_anchors]
