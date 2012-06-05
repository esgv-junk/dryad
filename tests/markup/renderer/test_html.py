from unittest import TestCase

from dryad.markup.plugins.emph      import Emph
from dryad.markup.plugins.list_     import List, ListItem
from dryad.markup.plugins.paragraph import Paragraph
from dryad.markup.plugins.root      import Root
#HACK from dryad.markup.plugins.section   import Section
from dryad.markup.plugins.strong    import Strong
from dryad.markup.plugins.table     import Table, TableCell, TableRow
from dryad.markup.plugins.text      import Text

from dryad.markup.renderer import render, push_renderer, pop_renderer

child_nodes = [Text(unicode(i)) for i in range(10)]

class BasicRenderTestCase(TestCase):
    def setUp(self):
        push_renderer('html')

    def tearDown(self):
        pop_renderer()

    def test_emph_rendering(self):
        render(Emph(child_nodes))
