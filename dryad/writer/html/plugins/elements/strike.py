from dryad.writer import str_nodes, render

strike_template = '<s>{{{child_text}}}</s>'

class Strike:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return render(strike_template, context)