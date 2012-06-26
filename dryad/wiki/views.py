# rendering
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect

# dryad markup
from dryad import markup
from dryad.wiki.path import get_parents
from dryad.wiki.models import *

# uploading
from django.core.files.storage import default_storage

# ==============================================================================
#                                    SHOW
# ==============================================================================

def show_page(request, path):
    page, _ = Page.get(path)
    if not page.source:
        return show_page_children(request, path)

    parents = get_parents(path)
    rendered_page = \
        markup.render(page.source, 'html', {'page_path': path})
    return render(request, 'show_page.html', locals())

# ==============================================================================
#                                    META
# ==============================================================================

def show_page_children(request, path):
    pages = Page.get(path)[0].children()
    parents = get_parents(path)
    rendered_page = render_to_string('list_pages.html', locals())
    return render(request, 'show_page.html', locals())

def show_page_files(request, path):
    return render(request, 'page_files.html', locals())

def upload_files(request, path):
    for file in request.FILES.getlist('upload'):
        save_path = path[1:] + '/' + file.name
        if default_storage.exists(save_path):
            return HttpResponse('Upload FAILED: ' + save_path + ' already exists')
        default_storage.save(save_path, file)

    return HttpResponse('Upload OK: ' + path)

def page_files(request, path):
    if request.method == 'GET':
        return show_page_files(request, path)
    else:
        return upload_files(request, path)

# ==============================================================================
#                                    EDIT
# ==============================================================================

def show_editor(request, path):
    page, _ = Page.get(path)
    return render(request, 'edit_page.html', locals())

def submit_page(request, path):
    page, page_is_new = Page.get(path)
    page.source = request.POST['source'].rstrip()

    if page.source:
        page.save()
    elif not page_is_new:
        if page.is_empty():
            page.delete()
        else:
            page.save()

    return HttpResponseRedirect('/wiki' + path)

def edit_page(request, path):
    if request.method == 'GET':
        return show_editor(request, path)
    else:
        return submit_page(request, path)

# =============== COOL EDIT ===================
from pyforge.all import *

def get_doctree(path):
    page, _ = Page.get(path)
    return markup.parse_document(page.source)

def get_child(root, need_index):
    from dryad.markup.plugins.list_ import List
    from dryad.markup.plugins.paragraph import Paragraph
    from dryad.markup.plugins.code import CodeBlock
    from dryad.markup.plugins.section import Section
    from dryad.markup.plugins.math_admonitions import MathAdmonitionBlock

    if isinstance(root, List):
        return root.items[need_index]

    true_index = 0
    index = 0
    while true_index < len(root.child_nodes):
        child = root.child_nodes[true_index]
        if isinstance(child, (List, Paragraph, CodeBlock, Section, MathAdmonitionBlock)):
            if index == need_index:
                return child
            index += 1
        true_index += 1

def get_node(root, node_path):
    if not node_path:
        return root
    return get_node(get_child(root, node_path[0]), node_path[1:])

def onpage_edit(request, path):

    if request.method == 'GET':
        lines = Page.get(path)[0].source.splitlines()
        doctree = get_doctree(path)
        node_path = map(int, request.GET['node_path'].split(','))
        node = get_node(doctree, node_path)

        lines = lines[node.src_start-1:node.src_end-1]
        lines = dedented_by(lines, get_min_indent(lines))
        node_lines = u'\n'.join(lines)

        return HttpResponse(node_lines, 'text/plain')

    else:
        page = Page.get(path)[0]
        lines = page.source.splitlines()
        doctree = get_doctree(path)
        node_path = map(int, request.POST['node_path'].split(','))
        node = get_node(doctree, node_path)

        node_lines = lines[node.src_start-1:node.src_end-1]
        min_indent = get_min_indent(node_lines)
        new_node_lines = indented_by(request.POST['new_lines'].split('\n'), min_indent)
        lines[node.src_start-1:node.src_end-1] = new_node_lines
        page.source = u'\n'.join(lines)
        page.save()

        return HttpResponse(lines, 'text/plain')

