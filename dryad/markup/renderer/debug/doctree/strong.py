from dryad.markup.renderer import *
import pystache

strong_template = '<strong>{{{child_text}}}</strong>'

class Strong:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return pystache.render(strong_template, context)
