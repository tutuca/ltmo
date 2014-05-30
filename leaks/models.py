# -*- coding: utf-8 -*-
import asyncio

from django.db import models
from taggit.managers import TaggableManager
from taggit.utils import parse_tags
from django.contrib.auth.models import User
from django.contrib import admin
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from markdown import markdown
from leaks.pipeline import start


class Leak(models.Model):
    slug = models.SlugField(editable=False, blank=True, null=True)
    title = models.CharField(max_length=126, blank=True, null=True)
    description = models.TextField()
    rendered = models.TextField(null=True, blank=True, editable = False)
    author = models.CharField(max_length=20, default='anon')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
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

        self.slug = '%s-%s' %(slugify(self.title[:30]) or 'sin-titulo', self.pk)
        super(Leak, self).save(*args, **kwargs)


class Attachment(models.Model):
    attachment_file = models.FileField(upload_to='leak_attachments')
    leak = models.ForeignKey('leaks.Leak')

    def preview(self):
        pass


class LeakAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags','author', 'created')
    list_filter = ('author', 'created')

admin.site.register(Leak, LeakAdmin)


@receiver(models.signals.post_save, sender=Leak)
def leak_post_processing(sender, **kwargs):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start(sender))
    loop.close()