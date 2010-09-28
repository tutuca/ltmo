from ltmo.models import Leak
from django import forms

class LeakForm(forms.ModelForm):
    class Meta:
        model = Leak

