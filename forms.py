from django import forms
from tagging.forms import TagField

from ltmo.models import Leak


class LeakForm(forms.ModelForm):
    tags = TagField(required=True)    
    class Meta:
        model = Leak
        exclude = ['rendered',]
