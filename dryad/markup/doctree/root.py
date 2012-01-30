class Root:
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    def __eq__(self, other):
        return isinstance(other, Root) and self.child_nodes == other.child_nodes

    doctree = ['child_nodes']
