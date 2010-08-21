from django.db import models
from tagging.fields import TagField
from django.template.defaultfilters import slugify

class Leak(models.Model):
    slug = models.SlugField(editable=False)
    description = models.TextField()
    author = models.CharField(max_length=20, default='Anonymous')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField(default='random,')
    def __unicode__(self):
        return self.description
        
    def save(self):
        self.slug = slugify(' '.join(self.description.split(' ')[:6]))
        super(Leak, self).save()


