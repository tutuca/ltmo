from django import forms
from tagging.forms import TagField

from leaks.models import Leak
from django.contrib.auth.models import User

class LeakForm(forms.ModelForm):
    tags = TagField(required=True)
    author = forms.CharField(widget=forms.HiddenInput, required=True)
    class Meta:
        model = Leak
        exclude = ['rendered','metadata']


from django import forms

class RegisterForm(forms.Form):
    
    honeypot = forms.CharField(widget=forms.HiddenInput, required=False)
    username = forms.SlugField()
    email = forms.EmailField()
    
    
    def clean_username(self):
        data = self.cleaned_data['username']
        try:
            user = User.objects.get(username=data)
        except User.DoesNotExist:
            user = None
            
        if user is not None:
            raise forms.ValidationError("El usuario ya existe")

        return data
