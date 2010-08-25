from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.sitemaps import Sitemap
from datetime import datetime
from tagging.fields import TagField

class Leak(models.Model):
    slug = models.SlugField(editable=False, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=20, default='Anonymous')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField(default='random')
    metadata = models.TextField()
    
    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('leak_detail', [self.id])
        
    def save(self):
        date = datetime.now().strftime("%d%H%M%S")
        self.slug = slugify(self.description[:42]+date)
        super(Leak, self).save()

class LTMOSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Leak.objects.all()

    def lastmod(self, obj):
        return obj.changed or obj.created



