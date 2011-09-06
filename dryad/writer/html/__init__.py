__all__ = []

from dryad import forge
from dryad import writer

def writeHTML(root, filename):
    #open file
    file = open(filename, 'wt', encoding = 'utf_8_sig')

    # set up emitters
    def emitRaw(text):
        nonlocal file
        file.write(text)

    def emit(text):
        emitRaw(forge.escapeHTML(text))

    writer.emit = emit
    writer.emitRaw = emitRaw
    writer.writer = 'html'

    # write header
    file.write(open('dryad/writer/html/header.html').read())

    # walk the doctree
    writer.walk(root)

    # write footer
    file.write(open('dryad/writer/html/footer.html').read())
