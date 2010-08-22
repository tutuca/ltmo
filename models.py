from django.db import models
from tagging.fields import TagField
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import simplejson as json

class JSONField(models.TextField):
    __metaclass__ = models.SubfieldBase
 
    def formfield(self, **kwargs):
        return super(JSONField, self).formfield(form_class=JSONFormField, **kwargs)
 
    def to_python(self, value):
        if isinstance(value, basestring):
            value = json.loads(value)
        return value
 
    def get_db_prep_save(self, value):
        if value is None: return
        return json.dumps(value)
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Leak(models.Model):
    slug = models.SlugField(editable=False, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=20, default='Anonymous')
    created = models.DateTimeField(auto_now_add=True, editable = False)
    changed = models.DateTimeField(auto_now=True, editable = False)
    tags = TagField(default='random')
    metadata = JSONField(blank=True, null= True)
    def __unicode__(self):
        return self.slug
        
    def save(self):
        date = datetime.now().strftime("%d%H%M%S")
        self.slug = slugify(' '.join(self.description.split(' ')[:4]))
        self.slug = self.slug + date
        super(Leak, self).save()


