from django import forms
from django.contrib.auth.models import User
from leaks.models import Leak


class LeakForm(forms.ModelForm):
    author = forms.CharField(widget=forms.HiddenInput, required=True)
    class Meta:
        model = Leak
        exclude = ['rendered','metadata']


class RegisterForm(forms.Form):
    #XXX: Should not be here.    
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
