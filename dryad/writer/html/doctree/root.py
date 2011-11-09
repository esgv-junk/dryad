from dryad.writer import *
import pystache

root_template_path = 'dryad/writer/html/doctree/root.mustache'

class Root:
    def write(self):
        context = {
            'child_lines': pystache_lines(
                str_nodes(*self.child_nodes)
            )
        }

        return pystache.render(
            open(root_template_path, 'r').read(), 
            context
        )