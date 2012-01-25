from dryad.markup.renderer import *
import pystache

emph_template = '<em>{{{child_text}}}</em>'

class Emph:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return pystache.render(emph_template, context)
