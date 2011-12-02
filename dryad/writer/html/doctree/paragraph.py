from dryad.writer import str_nodes, render

paragraph_template = '<p>{{{child_text}}}</p>'

class Paragraph:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return render(paragraph_template, context)