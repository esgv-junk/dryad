class List:
    def __init__(self, is_ordered, items):
        self.is_ordered = is_ordered
        self.items = list(items)
        for ord_number, item in enumerate(self.items):
            item.ord_number = ord_number

class ListItem:
    def __init__(self, item_num, child_nodes):
        self.value = item_num
        self.child_nodes = list(child_nodes)
        
def parse_list(block_name, inline_text, body_lines):
    pass
        
block_parsers = [('list', parse_list)]