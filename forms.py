from django.utils import simplejson as json
from django import forms

 
class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if not isinstance(value, basestring):
            value = json.dumps(value, indent=2)
        return super(JSONWidget, self).render(name, value, attrs)
 
class JSONFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = JSONWidget
        super(JSONFormField, self).__init__(*args, **kwargs)
 
    def clean(self, value):
        if not value: return
        try:
            return json.loads(value)
        except Exception, exc:
            raise forms.ValidationError(u'JSON decode error: %s' % (unicode(exc),))

class LeakForm(forms.ModelForm):
    metadata = JSONFormField()
    class Meta:
        model = Leak

