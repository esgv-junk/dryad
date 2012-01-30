from dryad.markup import *
from dryad.markup.renderer import *
from dryad.markup.doctree import *

document = """
=======
Heading
=======

Section
-------

Переносы!

I'm not twice the section I used to be
--------------------------------------

Cool story, bro
"""

def main():
    root = parse_document(document)
    print('--- from here ---')
    print(render_nodes(root, renderer='html'))

if __name__ == '__main__':
    main()
    print('Done')
