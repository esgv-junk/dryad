from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dryad.wiki.views',
    url(r'^wiki/(?P<name>[_a-zA-Z0-9]*)/?$', 'show_page'),
    url(r'^edit/(?P<name>[_a-zA-Z0-9]*)/?$', 'edit_page')
)
