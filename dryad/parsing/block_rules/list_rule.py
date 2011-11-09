import re
from dryad.parsing.utils.line_utils import *
from dryad.parsing.utils.k_iter import *
from dryad.doctree.block_nodes.list import List, ListItem


class UnorderedListRule:
    lookahead = 0
    
    start_re     = r'^\s*[\-\*] '
    capturing_re = r'^\s*([\-\*]) (.*)'
    
    @staticmethod
    def applies_to(source):
        return bool(re.match(UnorderedListRule.start_re, source[0]))
    
    @staticmethod
    def parse(source):
        for node in parse_list(source, is_ordered=False):
            yield node
            
        
int_re = r'0|[1-9][0-9]*'


class OrderedListRule:
    lookahead = 0
    
    start_re = r'^\s*(?:{int_re}|\#)[.)] '.format(int_re=int_re)
    capturing_re = r'^\s*({int_re}|\#)[.)] (.*)$'.format(int_re=int_re)
    
    @staticmethod
    def applies_to(source):
        return bool(re.match(OrderedListRule.start_re, source[0]))

    @staticmethod
    def parse(source):
        for node in parse_list(source, is_ordered=True):
            yield node
            
            
def parse_list(source, is_ordered):
    list_rule = is_ordered and OrderedListRule or UnorderedListRule
     
    start_indent = get_indent(source[0])

    items_lines = source.takewhile(
        lambda source: (
            get_indent(source[0]) > start_indent or 
            is_blank(source[0]) or (
                get_indent(source[0]) == start_indent and 
                list_rule.applies_to(source)
            )))
    
    yield List(
        is_ordered, 
        parse_list_items(items_lines, is_ordered)
    )
    
def parse_list_items(items_lines, is_ordered):
    source = k_iter(items_lines, lookahead=0)
    next(source, None)
    
    list_rule = is_ordered and OrderedListRule or UnorderedListRule

    while True:                                 # parse particular item                                 
        start_indent = get_indent(source[0])
        
        match_obj = re.match(list_rule.capturing_re, source[0])
        eat(source, 1)
    
        item_marker, first_line = match_obj.groups()
        item_num = (
            int(item_marker)
            if (is_ordered and item_marker != '#')  
            else None
        )
        item_body_lines = source.takewhile(
            lambda source: (
                get_indent(source[0]) > start_indent or 
                is_blank(source[0])
            ))
        item_all_lines = itertools.chain([first_line], item_body_lines)
        
        from dryad.parsing import parse_blocks, parse_spans
        yield ListItem(
            item_num, 
            parse_blocks(item_all_lines)
        )
        
        if source.is_done:
            break