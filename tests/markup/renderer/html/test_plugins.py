from unittest import TestCase, expectedFailure

from dryad.markup.renderer import render, push_renderer, pop_renderer
from dryad.markup.plugins.elements.code import CodeBlock

class PluginsHTMLRenderingTestCase(TestCase):
    def setUp(self):
        push_renderer('html')

    def tearDown(self):
        pop_renderer()

    def test_little_pygments_snippet(self):
        bad_snippet = ".GOTCHA"
        render(CodeBlock('auto', bad_snippet.splitlines()))
