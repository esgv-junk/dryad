from dryad.writer import str_nodes, render

link_template = '<a href={{href}}>{{body_text}}</a>'

class Link:
    def write(self):
        context = {
            'href'     : self.href,     
            'body_text': self.body_text or self.href
        }
        
        return render(link_template, context)