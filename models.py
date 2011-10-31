# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from tagging.fields import TagField
from tagging.utils import parse_tag_input

from django.contrib import admin
from django.template.defaultfilters import striptags, slugify
from markdown import markdown

class Leak(models.Model):
    slug = models.SlugField(editable=False, blank=True, null=True)
    title = models.CharField(max_length=126, default='sin-titulo')
    description = models.TextField()
    rendered = models.TextField(null=True, blank=True, editable = False)
    author = models.ForeignKey('auth.User', null=True)
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField()
    metadata = models.TextField(default='', null=True, blank=True)
    
    def __unicode__(self):
        return self.title or u'sin título'

    @models.permalink
    def get_absolute_url(self):
        try:
            tag = parse_tag_input(self.tags)[0]
        except IndexError:
            tag = self.tags #XXX: no tiene por qué dar IndexError, corregir los datos
            
        return ('leak_detail', [self.id])

    def save(self):
        self.rendered = markdown(
            self.description, 
            ['video', 'codehilite', 'urlize']
        )
        self.tags = ','.join([slugify(x) for x in parse_tag_input(self.tags)])
        self.slug = '%s-%s' %(slugify(self.title[:30]) or 'sin-titulo', self.pk)
        super(Leak, self).save()
        
class LeakAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags','author', 'created')
    list_filter = ('author', 'created')

admin.site.register(Leak, LeakAdmin)
