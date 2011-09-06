from dryad import doctree
from dryad import writer
from dryad.directives import math, code

# ========================== Default ================================

class Default(doctree.Inline):
    pass

def parseDefault(text):
    return Default(text)

def writeDefaultHTML(node):
    #math.writeMathInlineHTML(node)
    code.writeCodeInlineHTML(node)

writer.nodeWriters[Default, 'html'] = writeDefaultHTML
