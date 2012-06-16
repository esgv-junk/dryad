from dryad.markup.doctree import Node, Block, iter_find, walk, replace_node

class IdNode(Node):
    def __init__(self, node):
        self.node = node

    doctree = ['node']

def assign_unique_ids(root):
    id_ = 0
    for node in iter_find(root):
        node.id = id_
        id_ += 1

def wrap_into_id_block(node):
    if isinstance(node, Block):
        replace_node(node, IdNode(node))

def wrap_root_into_id_block(root):
    walk(root, wrap_into_id_block, skip_root=True)

AFTER_PARSE_DOCUMENT = [assign_unique_ids, wrap_root_into_id_block]
