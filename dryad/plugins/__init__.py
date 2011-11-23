from pyforge.all import *
from dryad import parsing

plugin_list = [
    'dryad.doctree.emph',                   # standart elements
    'dryad.doctree.list',
    'dryad.doctree.paragraph',
    'dryad.doctree.section',
    'dryad.doctree.strong',
    'dryad.doctree.text',
    
    'dryad.plugins.elements.code',          # advanced elements
    'dryad.plugins.elements.default_span', 
    'dryad.plugins.elements.image', 
    'dryad.plugins.elements.math_blocks', 
    'dryad.plugins.elements.math', 
    'dryad.plugins.elements.unknown',
    
    'dryad.plugins.settings',               # other plugins
    'dryad.plugins.typographer'
]

def load_plugins(*module_names):
    lists_to_gather = get_objects_names(parsing, list)
    
    for module_name in module_names:
        module = __import__(module_name, fromlist=[module_name])
        
        for list_name in lists_to_gather: 
            gather_list(module, list_name, parsing.__dict__)
        
load_plugins(*plugin_list)
