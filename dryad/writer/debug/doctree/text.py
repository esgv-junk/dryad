import pystache

class Text:
    def write(self):
        return pystache.render('{{body_text}}', body_text=self.body_text)        