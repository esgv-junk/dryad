from dryad.markup.doctree import find, type_selector, replace_node, create_doctree_structure

preferred_default_name = 'default'

class DefaultSpan:
    def __init__(self, body_text):
        self.body_text = body_text

    def __eq__(self, other):
        return (
            isinstance(other, DefaultSpan) and
            self.body_text == other.body_text
        )

class SetDefaultSpan:
    def __init__(self, default_span_name):
        self.default_span_name = default_span_name

    def __eq__(self, other):
        return(
            isinstance(other, SetDefaultSpan) and
            self.default_span_name == other.default_span_name
        )

def parse_default_span2(span_name, body_text):
    yield DefaultSpan(body_text)

def parse_set_default_span2(block_name, inline_text, body_text):
    yield SetDefaultSpan(inline_text.strip())

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

    for span_node in find(root, type_selector(DefaultSpan)):
        replace_node(
            span_node,
            parse_span(preferred_default_name, span_node.body_text)
        )

after_parse_document = [replace_default_spans]
block_parsers        = [('default_span', parse_set_default_span2)]
span_parsers         = [(''            , parse_default_span2)]
