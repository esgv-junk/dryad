from dryad import writer
from dryad.writer.html.tags import Tag

# =========================== Image =================================

class Image:
    def __init__(self, path):
        self.path = path

    def pformat(self, indent=0):
        return '{0}Image ({1})'.format('    '*indent, self.path)

def parseImage(inline, lines):
    return Image(inline)

def writeImageHTML(node):
    with Tag('div', _class='image', nospace=True):
        writer.emitRaw('<img src="{0}"/>\n'.format(node.path))
    writer.emitRaw('\n')

writer.nodeWriters[Image, 'html'] = writeImageHTML