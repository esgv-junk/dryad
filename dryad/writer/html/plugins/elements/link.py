from dryad.writer import str_nodes, render

link_template = '<a href={{href}}>{{{child_text}}}</a>'

class Link:
    def write(self):
        context = {
            'href'      : self.href,     
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return render(link_template, context)