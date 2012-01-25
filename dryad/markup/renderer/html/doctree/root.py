import glob, os
from dryad.markup.plugins.elements.toc import make_table_of_contents
from dryad.markup.renderer import render_nodes, render_template, pystache_files, pystache_list

root_template_path = 'dryad/markup/renderer/html/html_specific/templates/root.html'

class Root:
    def write(self):
                                            # add TOC to the first section
        self.child_nodes[0].child_nodes.insert(0, make_table_of_contents(self))
        
                                            # gather css files and scripts
        css_filenames = glob.glob('dryad/markup/renderer/html/html_specific/css/*.css')
        js_filenames  = glob.glob('dryad/markup/renderer/html/html_specific/js/*.js')
        
        context = {                         # create context
            'basename'    : os.getcwd(),                         
            'title'       : self.get_first_section_title() or '',
            'child_lines' : render_nodes(*self.child_nodes, sep='\n\n'),
            
            #'embedded_css': pystache_files(css_filenames, 'lines'),
            #'embedded_js' : pystache_files(js_filenames, 'lines'),
            'external_css': pystache_list(css_filenames, 'filename'),
            'external_js' : pystache_list(js_filenames, 'filename')
        }
                                            # renderer template
        return render_template(
            open(root_template_path, 'r').read(), 
            context
        )
