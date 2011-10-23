def setup_doctree_fields(root_node):
    if not hasattr(root_node, 'parent_node'):
        root_node.parent = None
    
    if hasattr(root_node, 'child_nodes'):
        for child_index in range(len(root_node.child_nodes)):
            # create some fields:
            # parent_node, child_index, next_sibling, prev_sibling
            child_node = root_node.child_nodes[child_index]
            child_node.parent_node = root_node
            child_node.child_index = child_index
            
            if child_index > 0:
                child_node.prev_sibling = root_node.child_nodes[child_index - 1]
            if child_index < (len(root_node.child_nodes) - 1):
                child_node.next_sibling = root_node.child_nodes[child_index + 1]

            # proceed
            setup_doctree_fields(child_node)

def walk_doctree(start_node, on_enter, on_exit):
    on_enter(start_node)
    if hasattr(start_node, 'child_nodes'):
        for child_node in start_node.child_nodes:
            walk_doctree(child_node, on_enter, on_exit)
    on_exit(start_node)