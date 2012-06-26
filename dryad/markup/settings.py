PLUGIN_LIST = [
    # First plugin, registering callbacks for creating doctree structure
    'dryad.markup.doctree',

    # default_span goes before section, because section renders its title_nodes
    # to get its ID, so default spans within title_nodes should already be
    # replaced at that moment
    'dryad.markup.plugins.default_span',
    'dryad.markup.plugins.section',

    # math should do its includes after default_span replacements have been
    # done.
    'dryad.markup.plugins.math',

    # strong should go before emph because of parsing rules
    'dryad.markup.plugins.strong',
    'dryad.markup.plugins.emph',

    # Shut down 'image' and 'link' from 'dryad.markup.plugins'
    'dryad.wiki.plugins.wiki_link',
    'dryad.wiki.plugins.wiki_image',

    'dryad.markup.plugins.list_',
    'dryad.markup.plugins.code',
    'dryad.markup.plugins.figure',
    'dryad.markup.plugins.math_admonitions',
    'dryad.markup.plugins.strike',
    #'dryad.markup.plugins.toc',

    # the later we do replaces, the better
    'dryad.markup.plugins.symbols',

    # paragraph and text should be last, since their parsing rules are
    # last-resort rules. 
    'dryad.markup.plugins.text',
    'dryad.markup.plugins.paragraph',
    
    # unknown should go even after text and paragraph: after all named 
    # blocks and spans
    'dryad.markup.plugins.unknown',

    # after all plugins have done their transformations, invoke tagger,
    # assigning unique IDs to all doctree nodes
    #'dryad.markup.plugins.id_wrapper'
]

MATH_DEFINES = ur'''
    \renewcommand{\Pr}{\mathop{\rm P}\nolimits}
    \newcommand{\ind}{\mathop{\rm I}\nolimits}
    \newcommand{\mean}{\mathop{\rm E}\nolimits}
    \newcommand{\var}{\mathop{\rm D}\nolimits}
    \newcommand{\cov}{\mathop{\rm cov}}

    \newcommand{\rank}{\mathop{\rm rank}\nolimits}
    \newcommand{\tr}{\mathop{\rm tr}\nolimits}
    \newcommand{\dim}{\mathop{\rm dim}\nolimits}
    \newcommand{\ker}{\mathop{\rm ker}\nolimits}
    \newcommand{\im}{\mathop{\rm im}\nolimits}

    \renewcommand{\liminf}{\mathop{\overline{\lim}}}
    \renewcommand{\limsup}{\mathop{\\underline{\lim}}}
    \newcommand{\to}{\mathop\longrightarrow}
    \newcommand{\implies}{\Rightarrow}
    \newcommand{\intl}{\int\limits}
    \newcommand{\iintl}{\iint\limits}
    \newcommand{\iiintl}{\iiint\limits}
    \newcommand{\d}{\partial}
    \renewcommand{\l}{\left}
    \renewcommand{\r}{\right}

    \renewcommand{\phi}{\varphi}
    \newcommand{\eps}{\varepsilon}
    \renewcommand{\emptyset}{\varnothing}
    \renewcommand{\mod}{\,\mathop{\rm mod}\,}
    \newcommand{\const}{\mathrm{const}}
'''

UNSET_DEFAULT_SPAN_NAME = u'default'
