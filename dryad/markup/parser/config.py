from pyforge.all import *
from dryad.markup.plugins import PLUGIN_LIST

BLOCK_PARSERS         = []
SPAN_PARSERS          = []
BEFORE_PARSE_DOCUMENT = []
AFTER_PARSE_DOCUMENT  = []

BLOCK_RULES = []
SPAN_RULES  = []

# load built-in rules
load_plugins([
    'dryad.markup.parser.rules.block_rule',
    'dryad.markup.parser.rules.span_rule',
], globals())

# load other plugins
load_plugins(PLUGIN_LIST, globals())
