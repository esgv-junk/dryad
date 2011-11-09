from dryad import doctree
from dryad import writer
from dryad.directives import math, code

class Default(doctree.Inline):
    def writeHTML(node):
        #math.writeMathInlineHTML(node)
        code.writeCodeInlineHTML(node)
        
    inlineParsers = {'': 'verbatim'}
    writers = {'html': writeHTML}

