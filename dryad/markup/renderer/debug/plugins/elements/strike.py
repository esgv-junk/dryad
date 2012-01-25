from dryad.markup.renderer import *
import pystache

emph_template = '<s>{{{child_text}}}</s>'

class Strike:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return pystache.render(strike_template, context)
