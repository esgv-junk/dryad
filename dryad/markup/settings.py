PLUGINS = [
    # First plugin, registering callbacks for creating doctree structure
    'dryad.markup.doctree',

    # default_span goes before section, because section renders its title_nodes
    # to get its ID, so default spans within title_nodes should already be
    # replaced at that moment
    'dryad.markup.plugins.default_span',

    # math should do its includes after default_span replacements have been done.
    'dryad.markup.plugins.math',

    'dryad.markup.plugins.emph',                   # standart elements
    'dryad.markup.plugins.paragraph',
    'dryad.markup.plugins.section',
    'dryad.markup.plugins.strong',
    'dryad.markup.plugins.text',

    'dryad.markup.plugins.code',                   # advanced elements
    'dryad.markup.plugins.figure',
    'dryad.markup.plugins.image',
    'dryad.markup.plugins.invisible',
    'dryad.markup.plugins.link',
    'dryad.markup.plugins.math_blocks',
    'dryad.markup.plugins.strike',
    'dryad.markup.plugins.symbols',
    'dryad.markup.plugins.toc',
    'dryad.markup.plugins.unknown',

    'dryad.markup.plugins.typographer'             # other plugins
]

MATH_INCLUDES = ur'''
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
    \renewcommand{\limsup}{\mathop{\underline{\lim}}}
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
