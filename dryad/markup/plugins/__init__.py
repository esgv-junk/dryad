PLUGIN_LIST = [
    # First plugin, registering callbacks for creating doctree structure
    'dryad.markup.doctree',

    # default_span goes before section, because section renders its title_nodes
    # to get its ID, so default spans within title_nodes should already be
    # replaced at that moment
    'dryad.markup.plugins.default_span',

    # math should do its includes after default_span replacements have been done.
    'dryad.markup.plugins.math',

    'dryad.markup.plugins.emph',                   # standart elements
    'dryad.markup.plugins.list_',
    'dryad.markup.plugins.paragraph',
    'dryad.markup.plugins.section',
    'dryad.markup.plugins.strong',
    'dryad.markup.plugins.text',

    'dryad.markup.plugins.code',                   # advanced elements
    'dryad.markup.plugins.figure',
    'dryad.markup.plugins.image',
    'dryad.markup.plugins.link',
    'dryad.markup.plugins.math_admonitions',
    'dryad.markup.plugins.strike',
    #'dryad.markup.plugins.toc',
    #'dryad.markup.plugins.unknown',

    #'dryad.markup.plugins.typographer'             # other plugins
]
