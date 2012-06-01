# rendering
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect

# dryad markup
from dryad import markup
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
    rendered_page = markup.render(page.source, renderer='html')
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
        if not page.children():
            page.delete()
        else:
            page.save()

    return HttpResponseRedirect('/wiki' + path)

def edit_page(request, path):
    if request.method == 'GET':
        return show_editor(request, path)
    else:
        return submit_page(request, path)

