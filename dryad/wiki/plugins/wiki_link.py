from dryad.markup.plugins.link import Link
from dryad.wiki.path import split_path, resolve_page_path, wiki_title

def parse_wiki_link(span_name, body_text):
    from dryad.markup import get_context

    if span_name == '@':
        span_name, body_text = body_text, ''

    # resolve href and get title, if a wiki link
    href = resolve_page_path(span_name, get_context()['page_path'])
    title = wiki_title(span_name[2:]) if span_name.startswith('w:') else ''

    return Link(href, body_text or title)

SPAN_PARSERS = [(u'^(@|[a-z]+:.*)$', parse_wiki_link)]
