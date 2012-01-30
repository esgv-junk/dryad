def true_selector(node):
    return True

def false_selector(node):
    return False

def type_selector(node_type):
     return lambda node: isinstance(node, node_type)
