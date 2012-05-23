import glob, os
from pyforge.all import *
from dryad.markup.doctree import find_first, type_selector
from dryad.markup.doctree.section import Section

def get_first_section(node):
    # TODO: just add to environment
    # TODO: need to move these cases to offline HTML renderer
    # TODO: assuming node exists
    return find_first(node, type_selector(Section))

basename = os.getcwd()

css_filenames = glob.glob('D:/Dropbox/code/dryad/dryad/markup/renderer/html/css/*.css')
js_filenames  = glob.glob('D:/Dropbox/code/dryad/dryad/markup/renderer/html/js/*.js')

css_content = list(map(read_text_file, css_filenames))
js_content = list(map(read_text_file, js_filenames))
