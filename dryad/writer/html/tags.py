from dryad import writer

def replaceKwd(d):
    if '_class' in d:
        d['class'] = d['_class']
        del d['_class']

spaceTags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
inlineTags = ['span', 'p', 'tt', 'em', 'strong',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

class Tag:
    def __init__(self, tag, nospace = None, inline = None, **attr):
        self.tag = tag
        self.inline = (tag in inlineTags) if (inline is None) else inline
        self.nospace = (tag not in spaceTags) if (nospace is None) else nospace

        self.attr = attr
        replaceKwd(self.attr)

    def __enter__(self):
        if not self.attr:
            writer.emitRaw('<{0}>'.format(self.tag))
        else:
            attrStr = ' '.join(
                '{0}="{1}"'.format(
                    key,
                    self.attr[key]
                        if isinstance(self.attr[key], str)
                        else ' '.join(self.attr[key]))
                for key in self.attr)

            writer.emitRaw('<{0} {1}>'.format(self.tag, attrStr))

        if not self.inline:
            writer.emitRaw('\n')
            if not self.nospace:
                writer.emitRaw('\n')

    def __exit__(self, exc_type, exc_value, traceback):
        writer.emitRaw('</{0}>'.format(self.tag))
        if not self.inline:
            writer.emitRaw('\n')

        if not self.nospace:
            writer.emitRaw('\n')