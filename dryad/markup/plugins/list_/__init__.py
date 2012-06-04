class List:
    def __init__(self, is_ordered, items):
        self.is_ordered = is_ordered
        self.items = list(items)

    doctree = ['items']

class ListItem:
    def __init__(self, item_num, child_nodes):
        self.value = item_num
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']
