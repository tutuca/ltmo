# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from tagging.fields import TagField
from tagging.utils import parse_tag_input
from django.contrib.auth.models import User
from django.contrib import admin
from django.template.defaultfilters import striptags, slugify
from markdown import markdown
from markdown_extensions import UrlizeExtension, VideoExtension


class Leak(models.Model):
    slug = models.SlugField(editable=False, blank=True, null=True)
    title = models.CharField(max_length=126, blank=True, null=True)
    description = models.TextField()
    rendered = models.TextField(null=True, blank=True, editable = False)
    author = models.SlugField(max_length=20, default='anon')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField()
    metadata = models.TextField(default='', null=True, blank=True)
    
    def __unicode__(self):
        return self.title or u'sin título'

    def get_user(self):
        try:
            user = User.objects.get(username=self.author)
        except User.DoesNotExist:
            user = None
        return user

    @models.permalink
    def get_absolute_url(self):
        return ('leak_detail', [self.id])

    def save(self):
        self.rendered = markdown(
            self.description, 
            [mdx_urlize, mdx_video, 'codehilite']
        )
        self.tags = ','.join([slugify(x) for x in parse_tag_input(self.tags)])
        self.slug = '%s-%s' %(slugify(self.title[:30]) or 'sin-titulo', self.pk)
        super(Leak, self).save()
        
class LeakAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags','author', 'created')
    list_filter = ('author', 'created')

admin.site.register(Leak, LeakAdmin)
