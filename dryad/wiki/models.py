from django.db import models
from django.contrib import admin
from dryad.wiki.path import split_path, join_path

class Page(models.Model):
    parent_path   = models.TextField(max_length=280)
    name          = models.TextField(max_length=140)
    source        = models.TextField(blank=True)

    created       = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering        = ['parent_path', 'name']
        unique_together = (('parent_path', 'name'),)

    def __unicode__(self):
        return join_path(self.parent_path, self.name)

    # ATTRIBUTES

    @staticmethod
    def get(path, name=None):
        if name is None:
            parent_path, name = split_path(path)

        try:
            return Page.objects.get(
                parent_path__iexact=parent_path,
                name__iexact=name
            ), False
        except Page.DoesNotExist:
            return Page(parent_path=parent_path, name=name), True

    def path(self):
        return join_path(self.parent_path, self.name)

    def parent(self):
        parent, has_no_parent = Page.get(self.parent_path)
        return None if has_no_parent else parent

    def children(self):
        return Page.objects.filter(parent_path__iexact=self.path())

    # INTEGRITY

    def save(self, *args, **kwargs):
        from dryad.wiki import views
        views.get_doctree.cache.pop(self.path())

        super(Page, self).save(*args, **kwargs)

        # if page is the root page, it has no parents
        if not self.name:
            return

        # create parents if they don't exist
        parent, has_no_parent = Page.get(self.parent_path)
        if has_no_parent and parent:
            parent.save()

    def is_empty(self):
        return not self.source and not self.children()

    def delete(self, *args, **kwargs):
        super(Page, self).delete(*args, **kwargs)

        self.children().delete()

        parent = self.parent()
        if parent:
            parent.delete_if_empty(*args, **kwargs)

    def delete_if_empty(self, *args, **kwargs):
        if self.is_empty():
            self.delete(*args, **kwargs)


class PageAdmin(admin.ModelAdmin):
    list_display  = ('name', 'parent_path', 'created', 'last_modified')
    list_filter   = ('created', 'last_modified')
    search_fields = ('name', 'parent_path')

admin.site.register(Page, PageAdmin)
