from dryad.doctree.span_nodes import pretty_format_spans
from dryad import writer

class Emph:
    def __init__(self, children):
        self.children = list(children)

    def pretty_format(self):
        return '<Emph>: {child_nodes}'.format(
            child_nodes=pretty_format_spans(*self.children, sep=' '))
        
    def enterHTML(self):
        writer.emitRaw('<em>')

    def exitHTML(self):
        writer.emitRaw('</em>')
        
    writers = {
        'HTML': (enterHTML, exitHTML)
    }