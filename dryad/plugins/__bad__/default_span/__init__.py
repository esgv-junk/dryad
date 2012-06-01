preferred_default_name = 'default'

class DefaultSpan:
    def __init__(self, body_text):
        self.body_text = body_text

class SetDefaultSpan:
    def __init__(self, default_span_name):
        self.default_span_name = default_span_name

def parse_default_span(span_name, body_text):
    yield DefaultSpan(body_text)

def parse_set_default_span(block_name, inline_text, body_text):
    yield SetDefaultSpan(inline_text.strip())

"""
def replace_default_spans(root):
    from dryad.markup.parser import parse_span

    for set_node in find(root, type_selector(SetDefaultSpan)):
        sib_index = set_node.sibling_index
        replace_node(set_node, [])

        for sibling in set_node.siblings[sib_index:]:
            if isinstance(sibling, SetDefaultSpan):
                break

            for span_node in find(
                sibling,
                type_selector(DefaultSpan),
                stop_siblings=type_selector(SetDefaultSpan)
            ):
                span_replace = list(
                    parse_span(set_node.default_span_name, span_node.body_text)
                )

                replace_node(span_node, span_replace)

    # replace nodes not in
    for span_node in find(root, type_selector(DefaultSpan)):
        new_span = parse_span(preferred_default_name, span_node.body_text)
        replace_node(span_node, new_span)

from dryad.markup.doctree import find, type_selector, replace_node, create_doctree_structure
"""

after_parse_document = [replace_default_spans]
block_parsers        = [('default_span', parse_set_default_span)]
span_parsers         = [(''            , parse_default_span)]
