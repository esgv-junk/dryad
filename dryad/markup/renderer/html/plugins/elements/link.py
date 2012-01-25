from dryad.markup.renderer import render_nodes, render_template

link_template = '<a href={{href}}>{{body_text}}</a>'

class Link:
    def write(self):
        context = {
            'href'     : self.href,     
            'body_text': self.body_text or self.href
        }
        
        return render_template(link_template, context)
