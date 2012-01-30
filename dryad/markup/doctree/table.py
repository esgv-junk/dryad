class Table:
    def __init__(self, rows):
        self.rows = list(rows)

    def __eq__(self, other):
        return isinstance(other, Table) and self.rows == other.rows

    doctree = ['rows']

class TableRow:
    def __init__(self, cells, vert_span=1):
        self.cells = list(cells)
        self.vert_span = vert_span

    def __eq__(self, other):
        return (
            isinstance(other, TableRow) and
            self.vert_span == other.vert_span and
            self.cells == other.cells
        )

    doctree = ['cells']
        
class TableCell:
    def __init__(self, child_nodes, is_header_cell=False, horiz_span=1):
        self.child_nodes = list(child_nodes)
        self.horiz_span = horiz_span
        self.is_header_cell = is_header_cell

    def __eq__(self, other):
        return (
            isinstance(other, TableCell) and
            self.is_header_cell == other.is_header_cell and
            self.horiz_span == other.horiz_span and
            self.child_nodes == other.child_nodes
        )

    doctree = ['child_nodes']
