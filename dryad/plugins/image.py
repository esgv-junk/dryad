class ImageBlock:
    def __init__(self, path):
        self.path = path
    
    @staticmethod
    def parse(block_name, inline_text, body_lines):
        path = inline_text.strip()
        yield ImageBlock(path)