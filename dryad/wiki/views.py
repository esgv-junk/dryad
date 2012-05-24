from django.shortcuts import render
from dryad.wiki.models import Page
from django.http import HttpResponse, HttpResponseRedirect
from dryad import markup

def get_page(name):
    return Page.objects.get_or_create(name=name)[0]

def show_page(request, name):
    rendered_page = markup.render(get_page(name).source, renderer='html')
    return render(request, 'show_page.html', locals())

def show_editor(request, name):
    source = get_page(name).source
    return render(request, 'edit_page.html', locals())

def submit_page(request, name):
    page = get_page(name)
    page.source = request.POST['source']
    page.save()
    return HttpResponseRedirect('/wiki/' + name)

def edit_page(request, name):
    if request.method == 'GET':
        return show_editor(request, name)
    else:
        return submit_page(request, name)
