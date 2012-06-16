from unittest import TestCase

from dryad.markup.doctree import link_doctree
from dryad.markup.plugins.text import Text
from dryad.markup.plugins.emph import Emph
from dryad.markup.plugins.section import Section, assign_section_levels_and_anchors
from dryad.markup.plugins.default_span import (
    SetDefaultSpan, DefaultSpan, replace_default_spans, preferred_default_name
    )

#                         SET UP CLASSES EQUALITY

skip_fields = set([
    'doctree',
    'parent',
    'siblings',
    'sibling_index',
    '_linked'
])

def equal(self, other):
    return all(
        field in other.__dict__ and
            self.__dict__[field] == other.__dict__[field]
        for field in self.__dict__
        if field not in skip_fields
    )

classes = [Text, Emph, Section]

for class_ in classes:
    class_.__eq__ = equal

#                                   TEST

from tests.markup.doctree.test_walker import doctree_structure_ok

class DefaultSpanTestCase(TestCase):
    def test_simple(self):
        root_node = Emph([
            SetDefaultSpan("text"),
            Text("1"),
            DefaultSpan("2")
        ])
        link_doctree(root_node)

        replace_default_spans(root_node)
        correct_node = Emph([Text("1"), Text("2")])

        self.assertEqual(root_node, correct_node)
        self.assertTrue(doctree_structure_ok(root_node))

    def test_not_set(self):
        from dryad.markup.parser import parse_span

        root_node = Emph([
            DefaultSpan("1")
        ])
        link_doctree(root_node)

        replace_default_spans(root_node)
        correct_node = Emph(
            list(parse_span(preferred_default_name, "1"))
        )

        self.assertEqual(root_node, correct_node)
        self.assertTrue(doctree_structure_ok(root_node))

    def test_horiz_scope(self):
        from dryad.markup.parser import parse_span

        root_node = Emph([
            DefaultSpan("1"),
            SetDefaultSpan("text"),
            DefaultSpan("2"),
            SetDefaultSpan("emph"),
            DefaultSpan("3")
        ])
        link_doctree(root_node)

        replace_default_spans(root_node)
        correct_node = Emph(
            list(parse_span(preferred_default_name, "1")) + [
                Text("2"),
                Emph([
                    Text("3")
                ])
            ])

        self.assertEqual(root_node, correct_node)
        self.assertTrue(doctree_structure_ok(root_node))

    def test_vert_scope(self):
        root_node = Emph([
            SetDefaultSpan("text"),
            DefaultSpan("1"),
            Emph([
                DefaultSpan("2"),
                SetDefaultSpan("emph"),
                DefaultSpan("3")
            ])
        ])
        link_doctree(root_node)

        replace_default_spans(root_node)
        correct_node = Emph([
            Text("1"),
            Emph([
                Text("2"),
                Emph([Text("3")])
            ])
        ])

        self.assertEqual(root_node, correct_node)
        self.assertTrue(doctree_structure_ok(root_node))

    def test_section_title(self):
        """
        Test default spans within section titles.

        Sections get their IDs by rendering their title_nodes. By that moment,
        default spans should already be replaced, since there is no renderer for
        DefaultSpan nodes. If they are not replaced, renderer could raise
        TemplateNotFound or just ignore DefaultSpan nodes, both are bad.
        """

        from dryad.markup.parser import parse_span

        root_node = Section([
            DefaultSpan("1")
        ], [])
        link_doctree(root_node)
        replace_default_spans(root_node)
        assign_section_levels_and_anchors(root_node)

        correct_node = Section(
            list(parse_span(preferred_default_name, "1")),
            []
        )

        self.assertEqual(root_node, correct_node)
        self.assertTrue(doctree_structure_ok(root_node))
