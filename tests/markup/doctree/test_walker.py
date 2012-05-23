from unittest import TestCase

from dryad.markup.doctree        import create_doctree_structure, replace_node
from dryad.markup.doctree.walker import walk, StopPropagation, StopWalk
from dryad.markup.doctree.emph   import Emph
from dryad.markup.doctree.text   import Text

class RaiseOnIndex:
    def __init__(self, index, exception):
        self.raise_index = index
        self.exception = exception
        self.index = 0

    def __call__(self, node):
        self.index += 1
        if self.raise_index + 1 == self.index:
            raise self.exception

class DoctreeTestCase(TestCase):
    def setUp(self):
        self.root_node = Emph([
            Emph([
                Text("1"),
                Text("2")
            ]),
            Text("3"),
            Text("4")
        ])

        self.all_nodes = [
            self.root_node,
            self.root_node.child_nodes[0],
            self.root_node.child_nodes[0].child_nodes[0],
            self.root_node.child_nodes[0].child_nodes[1],
            self.root_node.child_nodes[1],
            self.root_node.child_nodes[2]
        ]

def doctree_structure_ok(node,
                         parent=None,
                         siblings=None,
                         sibling_index=None):

    structure_ok = True

    try:
        structure_ok = structure_ok and (
            node.parent is parent and
            node.siblings is siblings and
            node.sibling_index == sibling_index
        )
    except AttributeError:
        structure_ok = False

    if not hasattr(node, 'doctree'):
        return structure_ok

    for child_name in node.doctree:
        child_nodes = getattr(node, child_name)

        if isinstance(child_nodes, list):
            siblings = child_nodes
        else:
            child_nodes = [child_nodes]
            siblings = None

        for sibling_index, child_node in enumerate(child_nodes):
            structure_ok = structure_ok and doctree_structure_ok(
                child_node,
                node,
                siblings,
                sibling_index if not (siblings is None) else None
            )

    return structure_ok

class DoctreeWalkerTestCase(DoctreeTestCase):

    def test_all_nodes(self):
        all_walk_nodes = list(walk(self.root_node))
        self.assertSequenceEqual(all_walk_nodes, self.all_nodes)

    def test_stop_propagation_1_level(self):
        walk_nodes = walk(
            self.root_node,
            RaiseOnIndex(1, StopPropagation())
        )
        correct_nodes = self.all_nodes[:1] + self.all_nodes[4:]
        self.assertSequenceEqual(list(walk_nodes), correct_nodes)

    def test_stop_propagation_2_levels(self):
        walk_nodes = walk(
            self.root_node,
            RaiseOnIndex(2, StopPropagation(2))
        )
        correct_nodes = self.all_nodes[:2] + self.all_nodes[4:]
        self.assertSequenceEqual(list(walk_nodes), correct_nodes)

    def test_stop_propagation_too_many_levels(self):
        for stop_index in range(len(self.all_nodes)):
            walk_nodes = walk(
                self.root_node,
                RaiseOnIndex(stop_index, StopPropagation(100))
            )
            correct_nodes = self.all_nodes[:stop_index]
            self.assertSequenceEqual(list(walk_nodes), correct_nodes)

    def test_stop_propagation_too_many_levels_raise(self):
        walk_nodes = walk(
            self.root_node,
            RaiseOnIndex(2, StopPropagation(100)),
            raise_stop_exceptions=True
        )
        correct_nodes = self.all_nodes[:2]
        for correct_node in correct_nodes:
            self.assertEqual(next(walk_nodes), correct_node)
        self.assertRaises(StopPropagation, next, walk_nodes)

    def test_stop_walk(self):
        for stop_index in range(len(self.all_nodes)):
            walk_nodes = walk(
                self.root_node,
                RaiseOnIndex(stop_index, StopWalk())
            )
            correct_nodes = self.all_nodes[:stop_index]
            self.assertSequenceEqual(list(walk_nodes), correct_nodes)

class DoctreeStructureTestCase(DoctreeTestCase):
    def setUp(self):
        super(DoctreeStructureTestCase, self).setUp()

        self.parents = [
            None,
            self.all_nodes[0],
            self.all_nodes[1],
            self.all_nodes[1],
            self.all_nodes[0],
            self.all_nodes[0]
        ]

        self.siblings = [
            None,
            self.all_nodes[0].child_nodes,
            self.all_nodes[1].child_nodes,
            self.all_nodes[1].child_nodes,
            self.all_nodes[0].child_nodes,
            self.all_nodes[0].child_nodes
        ]

        self.sibling_indices = [None, 0, 0, 1, 1, 2]

        create_doctree_structure(self.root_node)

    def test_doctree_strcture(self):
        for i, node in enumerate(self.all_nodes):
            self.assertIs(node.parent, self.parents[i])
            self.assertIs(node.siblings, self.siblings[i])
            self.assertEqual(node.sibling_index, self.sibling_indices[i])

        self.assertTrue(doctree_structure_ok(self.root_node))
        
    def test_replace_empty(self):
        correct_nodes = self.all_nodes[0:1] + self.all_nodes[4:]
        replace_node(self.all_nodes[1], [])
        walk_nodes = walk(self.root_node)

        self.assertSequenceEqual(list(walk_nodes), correct_nodes)
        self.assertTrue(doctree_structure_ok(self.root_node))

    def test_replace_single(self):
        target = Text("3")

        correct_nodes = self.all_nodes[:]
        correct_nodes[1:4] = [target]

        replace_node(self.all_nodes[1], target)
        walk_nodes = walk(self.root_node)

        self.assertSequenceEqual(list(walk_nodes), correct_nodes)
        self.assertTrue(doctree_structure_ok(self.root_node))

    def test_replace_multiple(self):
        target = [Text("3"), Text("4")]

        correct_nodes = self.all_nodes[:]
        correct_nodes[1:4] = target

        replace_node(self.all_nodes[1], target)
        walk_nodes = walk(self.root_node)

        self.assertSequenceEqual(list(walk_nodes), correct_nodes)
        self.assertTrue(doctree_structure_ok(self.root_node))

    def test_replace_hierarchical(self):
        target = Emph([Text("3")])

        correct_nodes = self.all_nodes[:]
        correct_nodes[1:4] = [target, target.child_nodes[0]]

        replace_node(self.all_nodes[1], target)
        walk_nodes = walk(self.root_node)

        self.assertSequenceEqual(list(walk_nodes), correct_nodes)
        self.assertTrue(doctree_structure_ok(self.root_node))


