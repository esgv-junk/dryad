from pyforge.all import *
from dryad.markup.doctree import iter_find, type_selector
from dryad.markup.plugins.text import Text

# CONFIG

typographic_escapes = {
    u'->' : u'\u2192',
    u'<-' : u'\u2190',
    u'<->': u'\u2194',
    u'--' : u'\u2014',    # em dash
    u'<<' : u'\u00ab',    # left double quote
    u'>>' : u'\u00bb'     # right double quote
}

typographic_replaces = {                # EXPERIMENTAL
    (u' - '     , u' \u2014 '),         # em dash
    (ur'"(.*?)"', u'\u00ab\\1\u00bb')   # automatic double quotes
}

# CORE

def typograph_text(text):
    text = multiple_replace(text, typographic_escapes)
    return multiple_replace_re(text, typographic_replaces)

def typograph_all_text(root):
    for node in iter_find(root, type_selector(Text)):
        node.body_text = typograph_text(node.body_text)

# PLUGIN

AFTER_PARSE_DOCUMENT = [typograph_all_text]


