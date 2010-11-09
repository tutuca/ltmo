from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from tagging.fields import TagField
from django.contrib import admin
from markdown import markdown
from django.template.defaultfilters import striptags

class Leak(models.Model):
    slug = models.SlugField(editable=False, unique=True)
    title = models.CharField(max_length=126, null=True, blank=True)
    description = models.TextField()
    rendered = models.TextField(null=True, blank=True, editable = False)
    author = models.CharField(max_length=20, default='Anonymous')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField(default='random')
    metadata = models.TextField()
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('leak_detail', [self.id])
        
    def save(self):
        if self.title == '':
            self.title = self.description[:70]
        now = datetime.now().strftime("%Y%R%N")
        self.rendered = markdown(self.description)
        self.slug = slugify('%s-%s' % (self.title[:30], now))
        super(Leak, self).save()
        
class LeakAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags','author', 'created')
    list_filter = ('author', 'created')

admin.site.register(Leak, LeakAdmin)
