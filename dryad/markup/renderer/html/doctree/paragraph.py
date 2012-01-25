from dryad.markup.renderer import render_nodes, render_template

paragraph_template = '<p>{{{child_text}}}</p>'

class Paragraph:
    def write(self):
        context = {
            'child_text': render_nodes(*self.child_nodes)
        }
        
        return render_template(paragraph_template, context)
