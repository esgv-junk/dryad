from dryad import doctree
from dryad import writer
from dryad.writer.html import tags

# ========================== Text ===================================

def textWriteHTML(node):
    writer.emit(node.text)

writer.nodeWriters[doctree.Text, 'html'] = textWriteHTML

# ========================= Strong ==================================

def strongEnterHTML(node):
    writer.emitRaw('<strong>')

def strongExitHTML(node):
    writer.emitRaw('</strong>')

writer.nodeWriters[doctree.Strong, 'html'] = \
    (strongEnterHTML, strongExitHTML)