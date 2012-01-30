class List:
    def __init__(self, is_ordered, items):
        self.is_ordered = is_ordered
        self.items = list(items)

    def __eq__(self, other):
        return (
            isinstance(other, List) and
            self.is_ordered == other.is_ordered and
            self.items == other.items
        )

    doctree = ['items']

class ListItem:
    def __init__(self, item_num, child_nodes):
        self.value = item_num
        self.child_nodes = list(child_nodes)

    def __eq__(self, other):
        return (
            isinstance(other, ListItem) and
            self.item_num == other.item_num and
            self.child_nodes == other.child_nodes
        )

    doctree = ['child_nodes']
