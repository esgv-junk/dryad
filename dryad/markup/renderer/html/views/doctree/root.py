import glob, os
from pyforge.all import *
from dryad.markup.doctree import find_first, type_selector
from dryad.markup.doctree.section import Section

def get_first_section(node):
    # TODO: just add to environment
    # TODO: need to move these cases to offline HTML renderer
    # TODO: assuming node exists
    return find_first(node, type_selector(Section))
