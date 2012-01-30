from pyforge.all import *

id_dispatcher = IdDispatcher()

def reset_id_dispatcher():
    global id_dispatcher
    id_dispatcher.clear()

from dryad.markup.doctree.walker.selectors import *
from dryad.markup.doctree.walker import *

def create_doctree_structure(node,
                             parent=None,
                             siblings=None,
                             sibling_index=None):

    node.parent = parent
    node.siblings = siblings
    node.sibling_index = sibling_index

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
            create_doctree_structure(
                child_node,
                node,
                siblings,
                sibling_index if not (siblings is None) else None
            )

def replace_node(node, dest):
    try:
        if node.siblings is None:
            raise NotImplementedError('No siblings.')

        node_parent = node.parent
        node_siblings = node.siblings
        src_index = node.sibling_index

        if hasattr(dest, '__iter__'):
            dest = list(dest)

            for dest_index, dest_node in enumerate(dest):
                create_doctree_structure(
                    dest_node,
                    node.parent,
                    node_siblings,
                    src_index + dest_index
                )

            node.siblings[src_index:src_index + 1] = dest

            untouched_siblings_start = src_index + len(dest)
            for i, sibling in enumerate(
                node_siblings[untouched_siblings_start:]
            ):
                sibling.sibling_index = untouched_siblings_start + i

        else:
            node.siblings[node.sibling_index] = dest
            create_doctree_structure(
                dest, node_parent, node_siblings, src_index
            )

    except AttributeError:
        raise ValueError('Node {0} is not a valid doctree node'.format(node))


before_parse_document = [reset_id_dispatcher]
after_parse_document  = [create_doctree_structure]
