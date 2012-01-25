from dryad.markup.renderer import render_nodes, render_template

strike_template = '<s>{{{child_text}}}</s>'

class Strike:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return render_template(strike_template, context)
