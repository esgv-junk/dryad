from dryad.writer import *
import pystache

emph_template = '<em>{{{child_text}}}</em>'

class Emph:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes, sep='')
        }
        
        return pystache.render(emph_template, context)