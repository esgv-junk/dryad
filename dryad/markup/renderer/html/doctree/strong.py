from dryad.markup.renderer import render_nodes, render_template

strong_template = '<strong>{{{child_text}}}</strong>'

class Strong:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return render_template(strong_template, context)
