class ImageBlock:
    def __init__(self, path):
        self.path = path

def parse_image(block_name, inline_text, body_lines):
    path = inline_text.strip()
    return ImageBlock(path)

block_parsers = [(u'image', parse_image)]

