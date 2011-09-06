from dryad import doctree
from dryad import writer
from dryad.writer.html.tags import Tag

# =========================== Section ===============================

headingLevel = 1

def sectionEnterHTML(node):
    global headingLevel

    writer.emitRaw('<div class="h{0}-outer">\n'.format(headingLevel))
    with Tag('h{0}'.format(headingLevel)):
        writer.walk(*node.titleNodes)
    writer.emitRaw('<div class="h{0}-inner">\n\n'.format(headingLevel))

    headingLevel += 1

def sectionExitHTML(node):
    global headingLevel
    writer.emitRaw('</div>\n</div>\n\n')
    headingLevel -= 1

writer.nodeWriters[doctree.Section, 'html'] = \
    (sectionEnterHTML, sectionExitHTML)

# ========================== Paragraph ==============================

def paragraphEnterHTML(node):
    writer.emitRaw('<p>')

def paragraphExitHTML(node):
    writer.emitRaw('</p>\n\n')

writer.nodeWriters[doctree.Paragraph, 'html'] = \
    (paragraphEnterHTML, paragraphExitHTML)

# ============================= List ================================

def listEnterHTML(node):
    writer.emitRaw('<div class="list {0}l">\n'.format(
        'o' if node.ordered else 'u'))
    writer.emitRaw('<{0}l>\n\n'.format(
        'o' if node.ordered else 'u'))

def listExitHTML(node):
    writer.emitRaw('</{0}l>\n</div>\n\n'.format(
        'o' if node.ordered else 'u'))

writer.nodeWriters[doctree.List, 'html'] = \
    (listEnterHTML, listExitHTML)

def listItemEnterHTML(node):
    writer.emitRaw('<li {1}class="{0}">\n\n'.format(
        'odd' if (node.childIndex % 2 == 0) else 'even',
        'value="{0}" '.format(node.value)
            if (node.value is not None)
            else ''))

def listItemExitHTML(node):
    writer.emitRaw('</li>\n\n')

writer.nodeWriters[doctree.ListItem, 'html'] = \
    (listItemEnterHTML, listItemExitHTML)