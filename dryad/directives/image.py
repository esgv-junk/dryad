from dryad import writer
from dryad.writer.html.tags import Tag

class Image:
    def __init__(self, name, inline, lines):
        self.path = inline

    def writeHTML(node):
        with Tag('div', _class='image', nospace=True):
            writer.emitRaw('<img src="{0}"/>\n'.format(node.path))
        writer.emitRaw('\n')
    
    blockParsers = {'image': 'empty'}
    writers = {'html': writeHTML}
    
    def pformat(self, indent=0):
        return '{0}Image ({1})'.format('    '*indent, self.path)
