from dryad.markup.renderer import render_nodes, render_template

emph_template = '<em>{{{child_text}}}</em>'

class Emph:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return render_template(emph_template, context)
