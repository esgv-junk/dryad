from dryad.writer import str_nodes, render

emph_template = '<em>{{{child_text}}}</em>'

class Emph:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return render(emph_template, context)