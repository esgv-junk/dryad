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
    'dryad.markup.plugins.table',
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

MATH_DEFINES = {
    'Pr':   r'\mathop{\rm P}\nolimits',
    'ind':  r'\mathop{\rm I}\nolimits',
    'mean': r'\mathop{\rm E}\nolimits',
    'var':  r'\mathop{\rm D}\nolimits',
    'cov':  r'\mathop{\rm cov}\nolimits',

    'rank': r'\mathop{\rm rank}\nolimits',
    'tr':   r'\mathop{\rm tr}\nolimits',
    'dim':  r'\mathop{\rm dim}\nolimits',
    'ker':  r'\mathop{\rm ker}\nolimits',
    'im':   r'\mathop{\rm im}\nolimits',

    'liminf':  r'\mathop{\overline{\lim}}',
    'limsup':  r'\mathop{\underline{\lim}}',
    'to':      r'\mathop\longrightarrow',
    'implies': r'\mathop\Rightarrow',
    'intl':    r'\int\limits',
    'iintl':   r'\iint\limits',
    'iiintl':  r'\iiint\limits',

    'd': r'\partial',
    'l': r'\left',
    'r': r'\right',

    'phi':      r'\varphi',
    'eps':      r'\varepsilon',
    'emptyset': r'\varnothing',
    'mod':      r'\,\mathop{\rm mod}\,',
    'const':    r'{\rm const}'
}

UNSET_DEFAULT_SPAN_NAME = u'default'
