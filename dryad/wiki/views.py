import codecs
from django.http import HttpResponse

from dryad.markup import *

def test_markup(request):
    path = ur'D:\Dropbox\knowledge\cs & math\algo\3_struct\4_hash.txt'
    source = codecs.open(path, encoding='utf-8-sig').readlines()
    return HttpResponse(parse_and_render_document(source, renderer='html'))

