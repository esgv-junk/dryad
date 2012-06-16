from dryad.markup.plugins.image import ImageBlock

# PARSE

def parse_wiki_image(block_name, inline_text, body_lines):
    path = inline_text.strip()
    return ImageBlock(path)

# PLUGIN


BLOCK_PARSERS = [(u'^image$', parse_wiki_image)]
