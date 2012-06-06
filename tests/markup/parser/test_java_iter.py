from unittest import TestCase
from dryad.markup.parser.java_iter import JavaIter

class JavaIterTestCase(TestCase):
    def setUp(self):
        self.lines = list(map(unicode, range(10)))
        self.padding = ''
        self.iter = JavaIter(self.lines, padding=self.padding)

    def test_iteration(self):
        lines_from_iter = list(self.iter)
        self.assertEqual(self.lines, lines_from_iter)

    def test_lookahead(self):
        for i in range(len(self.lines)):
            for lookahead in range(0, len(self.lines) / 2):
                if i + lookahead >= len(self.lines):
                    self.assertEqual(self.padding, self.iter[lookahead])
                else:
                    self.assertEqual(
                        self.lines[i + lookahead], self.iter[lookahead])

            self.assertEqual(self.lines[i], next(self.iter))

        self.assertRaises(StopIteration, lambda: next(self.iter))

    def test_position(self):
        self.assertEqual(self.iter.position(), 0)
        for pos, _ in enumerate(self.iter):
            self.assertEqual(self.iter.position(), pos + 1)

    def test_is_done(self):
        self.assertFalse(self.iter.is_done())
        for index, _ in enumerate(self.iter):
            if index == len(self.lines) - 1:
                self.assertTrue(self.iter.is_done())
            else:
                self.assertFalse(self.iter.is_done())
