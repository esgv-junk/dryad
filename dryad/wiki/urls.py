from django.conf.urls.defaults import patterns, url

page_name = '[_a-zA-Z0-9]+'
page_path = '(?P<path>(/{0})+)'.format(page_name)

urlpatterns = patterns('dryad.wiki.views',
    url(r'^$', 'show_page_children', {'path': ''}),
    url(r'^wiki{0}/?$'.format(page_path),  'show_page'),
    url(r'^edit{0}/?$'.format(page_path),  'edit_page'),
    url(r'^files{0}/?$'.format(page_path), 'page_files'),

    url(r'^children{0}/?$'.format(page_path), 'show_page_children')
)
