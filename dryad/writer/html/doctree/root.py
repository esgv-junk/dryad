import glob
import pystache

from dryad.doctree.section import Section
from dryad.writer import *

root_template_path = 'dryad/writer/html/doctree/root.txt'

class Root:
    def write(self):
        title = ''                          # gather title
        for node in self.child_nodes:
            if isinstance(node, Section):
                title = node.get_title_as_string()
                break
                                            # gather css files
        css_filenames = glob.glob('dryad/writer/html/css/*.css')
                
        context = {                         # create context                         
            'title': title,
            'stylesheets': pystache_list(css_filenames, 'filename'),
            'child_lines': pystache_lines(str_nodes(*self.child_nodes))
        }
                                            # render template
        return pystache.render(
            open(root_template_path, 'r').read(), 
            context
        )