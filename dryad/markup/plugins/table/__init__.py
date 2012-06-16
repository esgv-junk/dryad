from dryad.markup.doctree import Node, Block

class Table(Block):
    def __init__(self, rows):
        self.rows = list(rows)

    doctree = ['rows']

class TableRow(Node):
    def __init__(self, cells, vert_span=1):
        self.cells = list(cells)
        self.vert_span = vert_span

    doctree = ['cells']

class TableCell(Node):
    def __init__(self, child_nodes, is_header_cell=False, horiz_span=1):
        self.child_nodes = list(child_nodes)
        self.horiz_span = horiz_span
        self.is_header_cell = is_header_cell

    doctree = ['child_nodes']
