from dryad.markup.doctree import replace_node, iter_find, type_selector

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

def replace_default_spans(root):
    to_delete = []

    # starting from all SetDefaultSpan nodes in the doctree
    for set_node in iter_find(root, type_selector(SetDefaultSpan)):
        # queue for deletion
        sib_index = set_node.sibling_index
        to_delete.append(set_node)

        # for all following siblings
        for sibling in set_node.siblings[sib_index:]:
            if isinstance(sibling, SetDefaultSpan):
                break

            # find DefaultSpan nodes, breaking the search on SetDefaultSpan
            # nodes
            for span_node in iter_find(sibling, type_selector(DefaultSpan),
                  stop_siblings=type_selector(SetDefaultSpan)):

                # parse and replace
                from dryad.markup.parser import parse_span
                span_replace = \
                    parse_span(set_node.default_span_name, span_node.body_text)
                replace_node(span_node, span_replace)

    # replace DefaultSpan nodes, which were not affected by SetDefaultSpan
    for span_node in iter_find(root, type_selector(DefaultSpan)):
        new_span = parse_span(preferred_default_name, span_node.body_text)
        replace_node(span_node, new_span)

    # delete SetDefaultSpan nodes
    for set_node in to_delete:
        replace_node(set_node, [])

AFTER_PARSE_DOCUMENT = [replace_default_spans]
BLOCK_PARSERS        = [(u'^default_span$', parse_set_default_span)]
SPAN_PARSERS         = [(u'^$'            , parse_default_span)]
