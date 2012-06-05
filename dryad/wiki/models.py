from django.db import models
from django.contrib import admin

def get_parents(path):
    if path == '':
        return []
    parent_path, name = path.rsplit('/', 1)
    return get_parents(parent_path) + [(path, name)]

class Page(models.Model):
    path          = models.TextField(max_length=280, unique=True)
    source        = models.TextField(blank=True)
    created       = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ['path']

    def __unicode__(self):
        return self.path or '(ROOT PAGE)'

    # --------------------------------------------------------------------------
    #                              ATTRIBUTES
    # --------------------------------------------------------------------------

    def _split_path(self):
        return self.path.rsplit('/', 1)

    def name(self):
        return self._split_path()[1]

    @staticmethod
    def get(path):
        try:
            return Page.objects.get(path=path), False
        except Page.DoesNotExist:
            return Page(path=path), True

    def parent(self):
        try:
            parent_path, _ = self._split_path()
            return Page.objects.get(path=parent_path)
        except Page.DoesNotExist:
            return None

    def children(self):
        return Page.objects.filter(
            path__regex='^{0}/{1}$'.format(self.path, '[^/]+'))

    # --------------------------------------------------------------------------
    #                              INTEGRITY
    # --------------------------------------------------------------------------

    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)
        if not self.parent():
            parent_path = self._split_path()[0]
            if parent_path:
                Page(path=parent_path).save()

    def delete(self, *args, **kwargs):
        super(Page, self).delete(*args, **kwargs)
        self.children().delete()
        parent, parent_path = self.parent(), self._split_path()[0]
        while parent and not parent.source and not parent.children():
            parent.delete()
            parent = parent.parent()

class PageAdmin(admin.ModelAdmin):
    list_display  = ('path', 'created', 'last_modified')
    list_filter   = ('created', 'last_modified')
    search_fields = ('path',)

admin.site.register(Page, PageAdmin)



