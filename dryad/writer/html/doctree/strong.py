from dryad.writer import *
import pystache

strong_template = '<strong>{{{child_text}}}</strong>'

class Strong:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes, sep='')
        }
        
        return pystache.render(strong_template, context)