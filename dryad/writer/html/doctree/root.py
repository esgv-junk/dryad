import glob
import pystache
from dryad.doctree.section import Section
from dryad.writer import str_nodes, pystache_list

root_template_path = 'dryad/writer/html/html_specific/templates/root.txt'

class Root:
    def write(self):
        title = ''                          # gather title
        for node in self.child_nodes:
            if isinstance(node, Section):
                title = node.get_title_as_string()
                break
                                            # gather css files and scripts
        css_filenames = glob.glob('dryad/writer/html/html_specific/css/*.css')
        js_filenames = glob.glob('dryad/writer/html/html_specific/js/*.js');
                                            
        context = {                         # create context                         
            'title': title,
            'stylesheets': pystache_list(css_filenames, 'filename'),
            'scripts'    : pystache_list(js_filenames, 'filename'),
            'child_lines': str_nodes(*self.child_nodes)
        }
                                            # render template
        return pystache.render(
            open(root_template_path, 'r').read(), 
            context
        )