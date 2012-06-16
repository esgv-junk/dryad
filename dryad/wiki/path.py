from collections import namedtuple
from django.core.files.storage import default_storage

SplitPath = namedtuple('SplitPath', ('parent_path', 'name'))

def split_path(path):
    if not path:
        return SplitPath('', '')
    if '/' in path:
        return SplitPath(*path.rsplit('/', 1))
    else:
        return SplitPath('', path)

def join_path(parent_path, name):
    if not (parent_path or name):
        return ''
    return parent_path + '/' + name

def get_parents(path, name=None):
    """
    Usage: get_parents(path)
           get_parents(parent_path, name)
    """
    if not name:
        if path == '':
            return [('', '')]
        path, name = path.rsplit('/', 1)
    return get_parents(path) + [(path, name)]

def get_parent_paths(path, name=None):
    if not name:
        if path == '':
            return ['']
        path, name = path.rsplit('/', 1)
    return get_parent_paths(path) + [join_path(path, name)]

def resolve_page_path(path, current_page_path):
    from dryad.wiki.models import Page

    # leave as-is, if not a wiki path
    if not path.startswith(u'w:'):
        return path
    else:
        # strip 'w:' and replace spaces
        path = path[2:].replace(' ', '_')
        
    # absolute path
    if path.startswith(u'/'):
        return u'/wiki' + path

    # relative path; search page itself and parents
    parents = get_parent_paths(current_page_path)
    for parent in reversed(parents):
        trial_path = join_path(parent, path)
        _, not_exists = Page.get(trial_path)
        if not not_exists:
            return u'/wiki' + trial_path

    # try search by name
    name = split_path(path).name
    try:
        page = Page.objects.get(name__exact=name)
        return u'/wiki' + page.path()
    except (Page.MultipleObjectsReturned, Page.DoesNotExist):
        pass

    # return link to current page's child
    return u'/wiki' + join_path(current_page_path, path)

def resolve_image_path(img_path, current_page_path):
    if not img_path.startswith(u'w:'):
        return img_path
    else:
        # strip 'w:'
        img_path = img_path[2:]

    local_prefix = '/media'
    if not img_path.startswith(u'/'):
        local_prefix += page_path + '/'

    # absolute path
    if img_path.startswith(u'/'):
        return u'/media' + img_path

    # relative path; search page itself and parents
    parents = get_parent_paths(current_page_path)
    for parent in reversed(parents):
        trial_path = join_path(parent, img_path)
        if default_storage.exists(trial_path):
            return u'/media' + trial_path

    # return link to current page's child
    return u'/media' + join_path(current_page_path, img_path)


def wiki_title(path):
    return split_path(path).name.replace('_', ' ')





