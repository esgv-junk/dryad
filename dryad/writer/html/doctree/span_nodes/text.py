import pystache

class Text:
    def write(self):
        return pystache.render('{{text}}', text=self.text)