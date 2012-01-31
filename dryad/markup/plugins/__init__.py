plugin_list = [
    # default_span goes before section, because section renders its title_nodes
    # to get its ID, so default spans within title_nodes should already be
    # replaced at that moment
    'dryad.markup.plugins.elements.default_span',

    'dryad.markup.doctree',                        # standart elements
    'dryad.markup.doctree.emph',                   
    'dryad.markup.doctree.list_',
    'dryad.markup.doctree.paragraph',
    'dryad.markup.doctree.section',
    'dryad.markup.doctree.strong',
    'dryad.markup.doctree.text',
    
    'dryad.markup.plugins.elements.code',          # advanced elements
    'dryad.markup.plugins.elements.figure',
    'dryad.markup.plugins.elements.image',
    'dryad.markup.plugins.elements.invisible',
    'dryad.markup.plugins.elements.link',
    'dryad.markup.plugins.elements.math_blocks', 
    'dryad.markup.plugins.elements.math', 
    'dryad.markup.plugins.elements.strike',
    'dryad.markup.plugins.elements.symbols',
    'dryad.markup.plugins.elements.toc',
    'dryad.markup.plugins.elements.unknown',
    
    'dryad.markup.plugins.typographer'             # other plugins
]
