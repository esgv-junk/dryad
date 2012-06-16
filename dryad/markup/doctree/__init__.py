from dryad.markup.doctree.walker import *

class Node:
    pass

class Span(Node):
    pass

class Block(Node):
    pass

def link_doctree(node, parent=None, siblings=None, sibling_index=None):
    """
    Create 3 fields on each node: parent, siblings and sibling_index.

    If node has no siblings (standalone field), then siblings and sibling_index
    will both be None.

    """
    node.parent = parent
    node.siblings = siblings
    node.sibling_index = sibling_index if siblings is not None else None
    node._linked = True

    if not hasattr(node, 'doctree'):
        return

    for child_name in node.doctree:
        child_nodes = getattr(node, child_name)

        if isinstance(child_nodes, list):
            siblings = child_nodes
        else:
            child_nodes = [child_nodes]
            siblings = None

        for sibling_index, child_node in enumerate(child_nodes):
            if hasattr(child_node, '_linked') and child_node._linked:
                # a child is already linked
                # possibly, link_doctree(node) has already been called, but
                # someone else now just needed to replace siblings_index
                continue
            link_doctree(child_node, node, siblings, sibling_index)

def replace_node(node, dest):
    try:
        parent = node.parent
        siblings = node.siblings
        src_index = node.sibling_index
    except AttributeError:
        raise ValueError('Node {0} is not a valid doctree node'.format(node))

    if node.siblings is None:
        raise NotImplementedError(
            "Can't replace node, when there are no siblings.")

    # replace one node with many
    if hasattr(dest, '__iter__'):
        dest = list(dest)

        # link new nodes with correct sibling_index
        for dest_index, dest_node in enumerate(dest):
            link_doctree(dest_node, parent, siblings, src_index + dest_index)

        # replace old node
        node.siblings[src_index:src_index + 1] = dest

        # correct other siblings' indices
        old_siblings_start = src_index + len(dest)
        for i, old_sibling in enumerate(siblings[old_siblings_start:]):
            old_sibling.sibling_index = old_siblings_start + i

    # simply replace one node with one node
    else:
        node.siblings[node.sibling_index] = dest
        link_doctree(dest, parent, siblings, src_index)

AFTER_PARSE_DOCUMENT = [link_doctree]
