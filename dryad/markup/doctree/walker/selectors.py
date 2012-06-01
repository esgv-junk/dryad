def true_selector(node):
    return True

def false_selector(node):
    return False

def type_selector(*node_types):
    return lambda node: isinstance(node, node_types)

def nth_child(n):
    return lambda node: False
