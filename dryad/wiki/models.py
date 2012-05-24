from django.db import models
from django.contrib import admin

class Page(models.Model):
    name          = models.SlugField(max_length=140, unique=True)
    source        = models.TextField(blank=True)
    created       = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'last_modified')

admin.site.register(Page, PageAdmin)



