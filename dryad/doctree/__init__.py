__all__ = []

from . block_nodes import Block, Root, Paragraph, Section, List, ListItem
from . inline_nodes import Inline, Text, Strong

def fixHierarchy(node):
    if not hasattr(node, 'parent'):
        node.parent = None
    
    if hasattr(node, 'children'):
        childIndex = 0

        for i in range(len(node.children)):
            # create some fields:
            # parent, childIndex, nextSibling, prevSibling
            child = node.children[i]
            child.parent = node
            child.childIndex = childIndex
            if i > 0:
                child.prevSibling = node.children[i-1]
            if i < len(node.children)-1:
                child.nextSibling = node.children[i+1]

            # proceed
            fixHierarchy(child)
            childIndex += 1

def walkDoctree(node, enter, exit):
    enter(node)
    if hasattr(node, 'children'):
        for c in node.children:
            walkDoctree(c, enter, exit)
    exit(node)