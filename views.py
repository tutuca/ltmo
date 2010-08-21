from django.views.generic import list_detail, simple
from ltmo.models import Leak
from django.conf import settings
from django import forms
import json
class LeakForm(forms.ModelForm):
    class Meta:
        model = Leak

def index(request):
    return list_detail.object_list(
        request,
        Leak.objects.all(),
        template_name='index.html',

    )

def new_post(request):
    
    if request.method == 'POST':
        post = json.loads(request.POST.keys()[0])
        form = LeakForm(request)
        import ipdb; ipdb.set_trace()        
        if form.is_valid():
            leak = form.save(commit=False)
            admins = settings.ADMINS
            
            author = [author for author in admins if leak.author==author[0]]
            leak.author = author
            leak.save()
    else:
        form = LeakForm()
        
    return simple.direct_to_template(
        request,
        'success.json', 
        mimetype='application/json',
        extra_context={
            'form':form,
        }
    )
