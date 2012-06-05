from unittest import TestCase
from dryad.markup.parser.lookahead_iter import LookaheadIter
from dryad.markup.parser import skip_blank_lines, take_nonblank_lines

non_empty_lines = [unicode(i) for i in range(10)]

class ParserUtilitiesTestCase(TestCase):
    def test_skip_empty(self):
        lines = [''] * 10 + non_empty_lines
        iter = LookaheadIter(lines, padding='')
        skip_blank_lines(iter)
        self.assertEqual(iter.position(), 10)

    def test_take_nonempty(self):
        lines = non_empty_lines + [''] * 10 + non_empty_lines
        iter = LookaheadIter(lines, padding='$')

        self.assertEqual(take_nonblank_lines(iter), non_empty_lines)
        self.assertEqual(iter.position(), len(non_empty_lines))

        skip_blank_lines(iter)

        self.assertEqual(take_nonblank_lines(iter), non_empty_lines)
        self.assertTrue(iter.is_done())
