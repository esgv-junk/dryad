class ImageBlock:
    def __init__(self, path):
        self.path = path
    
def parse_image(block_name, inline_text, body_lines):
    path = inline_text.strip()
    yield ImageBlock(path)
    
block_parsers = [('image', parse_image)]

