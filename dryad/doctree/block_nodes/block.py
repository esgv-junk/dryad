class Block:
    def __init__(self, block_name, inline_text, body_lines):
        self.block_name = block_name
        self.inline_text = inline_text
        self.body_lines = list(body_lines)