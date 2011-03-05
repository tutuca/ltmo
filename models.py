# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from tagging.fields import TagField
from django.contrib import admin
from markdown import markdown
from django.template.defaultfilters import striptags, slugify, urlize
from ltmo.templatetags.urlparser import url_to_img


class Leak(models.Model):
    slug = models.SlugField(editable=False, blank=True, null=True)
    title = models.CharField(max_length=126, null=True, blank=True)
    description = models.TextField()
    rendered = models.TextField(null=True, blank=True, editable = False)
    author = models.CharField(max_length=20, default='Anonymous')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField()
    metadata = models.TextField(default='', null=True, blank=True)
    
    def __unicode__(self):
        return self.title or u'sin título'

    @models.permalink
    def get_absolute_url(self):
        return ('leak_detail', [self.id])
        
    def save(self):
        self.rendered = markdown(urlize(url_to_img(self.description)), ['codehilite'])
        slug_text = self.title[:30] or u'sin título'
        self.slug = slugify(slug_text)
        super(Leak, self).save()
        
class LeakAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags','author', 'created')
    list_filter = ('author', 'created')

admin.site.register(Leak, LeakAdmin)
