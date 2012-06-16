# -*- coding: utf-8 -*-

from dryad.markup import *
from dryad.markup.renderer import *
from dryad.markup.doctree import *
from dryad.markup.plugins.text import Text

document = unicode("""
Section
-------

Переносы!""", 'utf-8')


def main():
    root = parse_document(document)
    print('--- from here ---')
    print(render_nodes(root, renderer='html'))

if __name__ == '__main__':
    main()
    print('Done')
