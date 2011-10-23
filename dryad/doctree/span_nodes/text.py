class Text:
    def __init__(self, text):
        self.text = text
    
    def pretty_format(self):
        return '<Text> /{text}/'.format(
            text=self.text)
        
    def writeHTML(node):
        writer.emit(node.text)

    writers = {
        'HTML': writeHTML
    }