from dryad.parsing.utils.str_utils import *
from dryad.doctree.block_nodes import pretty_format_blocks
from dryad.writer import emit, emit_raw

class List:
    def __init__(self, is_ordered, child_nodes):
        self.is_ordered = is_ordered
        self.child_nodes = list(child_nodes)

    def pretty_format(self, indent_level = 0):
        return (make_indent(indent_level) + 
                '<List> ({ordered})\n'.format(
                    ordered='is_ordered' if self.is_ordered else 'unordered') +
                pretty_format_blocks(*self.child_nodes, 
                                     indent_level=indent_level+1))
        
    def enterHTML(self):
        emit_raw(
            '''\
            <div class="list {ordered}l">
            <{ordered}l>
            
            '''.format(
                ordered='o' if self.is_ordered else 'u'))
    
    def exitHTML(self):
        emit_raw(
            '''\
            </{ordered}l>
            </div>
            
            '''.format(
                ordered='o' if self.is_ordered else 'u'))
    
    writers = {
        'HTML': (enterHTML, exitHTML)
    }
    
    
    
class ListItem:
    def __init__(self, item_num, child_nodes):
        self.value = item_num
        self.child_nodes = list(child_nodes)

    def pretty_format(self, indent_level = 0):
        return (make_indent(indent_level) + 
                '<ListItem> {item_num}\n'.format(
                    item_num=self.value) +
                pretty_format_blocks(*self.child_nodes, 
                                     indent_level=indent_level+1))
        
    def enterHTML(node):
        emit_raw(
            '''\
            <li {value}class="{odd}">
            
            '''.format(
                odd='odd' if (node.child_index % 2 == 0) else 'even',
                value='value="{item_num}" '.format(node.item_num)
                    if (node.item_num is not None)
                    else ''))

    def exitHTML(node):
        emit_raw(
            '''\
            </li>
            
            ''')

    writers = {
        'HTML': (enterHTML, exitHTML)
    }    
    
        