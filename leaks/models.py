# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from markdown import markdown
from leaks.mdx_urlize import makeExtension as make_urlize
from leaks.mdx_video import makeExtension as make_video


class Leak(models.Model):
    slug = models.SlugField(editable=False, blank=True, null=True)
    title = models.CharField(max_length=126, blank=True, null=True)
    description = models.TextField()
    rendered = models.TextField(null=True, blank=True, editable=False)
    author = models.CharField(max_length=20, default='anon')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    changed = models.DateTimeField(auto_now=True, editable=False)
    tags = TaggableManager()
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

    def save(self, *args, **kwargs):
        self.rendered = markdown(
            self.description,
            [make_urlize(), make_video(), 'codehilite']
        )
        self.slug = '%s-%s' % (slugify(self.title[:30]) or 'sin-titulo', self.pk)
        super(Leak, self).save(*args, **kwargs)
