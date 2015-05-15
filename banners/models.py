# -*- coding: utf-8 -*-

from django.db import models
from taggit.managers import TaggableManager
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.template import Context, Template


class Banner(models.Model):
    code = models.TextField(max_length=1024, blank=True, null=True)
    slot = TaggableManager()
    clicks = models.PositiveIntegerField(default=0, blank=True)
    views = models.PositiveIntegerField(default=0, blank=True)

    def __unicode__(self):
        return "Banner #%s on %s" % (self.pk, self.slot)

    def render_code(self):
        template = Template(self.code)
        return template.render(Context({'object': self, }))


class TemplateBanner(Banner):
    image = models.ImageField(upload_to='banners', null=True)
    url = models.URLField(blank=True)
    template = models.CharField(max_length=70, default='banner.html')

    def __unicode__(self):
        return "%s" % (slugify(self.pk, self.slot),)

    def show_in_list(self):
        self.views += 1
        return render_to_string(
            self.template,
            {
                'object': self,
            }
        )
