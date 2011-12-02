from dryad.writer import str_nodes, render

strong_template = '<strong>{{{child_text}}}</strong>'

class Strong:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return render(strong_template, context)