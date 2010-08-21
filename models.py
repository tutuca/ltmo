from django.db import models
from tagging.fields import TagField
from django.template.defaultfilters import slugify
from datetime import datetime
class Leak(models.Model):
    slug = models.SlugField(editable=False, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=20, default='Anonymous')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField(default='random,')
    
    def __unicode__(self):
        return self.slug
        
    def save(self):
        date = datetime.now().strftime("%d%H%M%S")
        self.slug = slugify(' '.join(self.description.split(' ')[:4]))
        self.slug = self.slug + date
        super(Leak, self).save()


