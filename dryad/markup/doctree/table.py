class Table:
    def __init__(self, rows):
        self.rows = list(rows)
        for ord_number, row in enumerate(self.rows, 1):
            row.ord_number = ord_number
        
class TableRow:
    def __init__(self, cells, vert_span=1):
        self.cells = list(cells)
        self.vert_span = vert_span
        
class TableCell:
    def __init__(self, child_nodes, is_header_cell=False, horiz_span=1):
        self.child_nodes = list(child_nodes)
        self.horiz_span = 1
        self.is_header_cell = is_header_cell