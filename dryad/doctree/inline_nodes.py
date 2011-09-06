class Inline:
    def __init__(self, text):
        self.text = text

    def pformat(self):
        return '({0}: {1})'.format(type(self), self.text)

class Text(Inline):
    pass

class Strong:
    def __init__(self, children):
        self.children = list(children)

    def pformat(self):
        return '({0}: {1})'.format(type(self), 'write pformat!')
