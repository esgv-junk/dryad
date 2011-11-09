import re
from dryad.parsing.utils.line_utils import *
from dryad.parsing.utils.k_iter import *
from dryad.doctree.block_nodes.section import Section
 

class SectionRule2:
    lookahead = 1
    
    @staticmethod
    def applies_to(source):
        return title_matches_outline(source[0], source[1])
        
    @staticmethod
    def extract_heading_attributes(source):
        """Returns (title, heading_char, num_lines_heading_takes)"""
        
        return (source[0], source[1][0:1], 2)
    
    @staticmethod
    def parse(source):
        for node in parse_section(SectionRule2, source):
            yield node
            
            
class SectionRule3:
    lookahead = 2
    
    @staticmethod
    def applies_to(source):
        return (title_matches_outline(source[1], source[0]) and
                source[2] == source[0])
        
    @staticmethod
    def extract_heading_attributes(source):
        """Returns (title, heading_char, num_lines_heading_takes)"""
        
        return (source[1], source[0][0:1], 3)
    
    @staticmethod
    def parse(source):
        for node in parse_section(SectionRule3, source):
            yield node
    
            
def title_matches_outline(title, outline):
    indents_match = (get_indent(title) == get_indent(outline) == 0)
    
    outline_re = "^{char}{{{min_repeats},}}$".format(
        char='[=\-]',
        min_repeats=len(title)
    )
    
    return (
        indents_match and
        not is_blank(title) and
        re.match(outline_re, outline)
    )
    
def parse_section(section_rule, source):
    title, outline_char, num_lines_heading_takes = \
        section_rule.extract_heading_attributes(source)
    
    eat(source, num_lines_heading_takes)
    
    def is_next_same_level_section_start(source):
        nonlocal section_rule, outline_char
        
        current_outline_char = \
            section_rule.extract_heading_attributes(source)[1]
            
        return (outline_char == current_outline_char and
                section_rule.applies_to(source))
    
    body_lines = source.takewhile(
        lambda s: not is_next_same_level_section_start(s))
    
    from dryad.parsing import parse_blocks, parse_spans
    
    title_nodes = parse_spans(title)
    child_nodes = parse_blocks(body_lines)
    yield Section(title_nodes, child_nodes)
