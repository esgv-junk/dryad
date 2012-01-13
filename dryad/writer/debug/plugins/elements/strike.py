from dryad.writer import *
import pystache

emph_template = '<s>{{{child_text}}}</s>'

class Strike:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return pystache.render(strike_template, context)    