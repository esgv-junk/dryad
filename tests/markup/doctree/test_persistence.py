from unittest import TestCase
from pyforge.all import *

from dryad.markup.plugins.emph      import Emph
from dryad.markup.plugins.list_     import List, ListItem
from dryad.markup.plugins.paragraph import Paragraph
from dryad.markup.plugins.root      import Root
#HACK from dryad.markup.plugins.section   import Section
from dryad.markup.plugins.strong    import Strong
from dryad.markup.plugins.table     import Table, TableCell, TableRow
from dryad.markup.plugins.text      import Text

make_child_nodes = lambda: (Text(i) for i in range(10))

class Class:
    pass

class DoctreePersistenceTestCase(TestCase):
    def _test_node(self, node, child_nodes_name='child_nodes'):
        if (type(node) is type(Class)):
            node = node(**{child_nodes_name: make_child_nodes()})
        eat(getattr(node, child_nodes_name))
        self.assertSequenceEqual(
            list(make_child_nodes()),
            list(getattr(node, child_nodes_name))
        )

    def test_emph(self):
        self._test_node(Emph)

    def test_emph(self):
        self._test_node(Emph)

    def test_list(self):
        self._test_node(List(False, make_child_nodes()), 'items')
        self._test_node(ListItem(None, make_child_nodes()))

    def test_paragraph(self):
        self._test_node(Paragraph)

    def test_root(self):
        self._test_node(Root)

    def test_section(self):
        node = Section(make_child_nodes(), make_child_nodes())
        self._test_node(node, 'title_nodes')
        self._test_node(node, 'child_nodes')

    def test_strong(self):
        self._test_node(Strong)

    def test_table(self):
        self._test_node(Table, 'rows')
        self._test_node(TableRow, 'cells')
        self._test_node(TableCell)
