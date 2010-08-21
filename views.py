from django.views.generic import list_detail, simple
from ltmo.models import Leak
from django.conf import settings
from django import forms
import json
class LeakForm(forms.ModelForm):
    class Meta:
        model = Leak

def index(request):
    ordering = request.GET.get('order','-created')
    return list_detail.object_list(
        request,
        Leak.objects.all().order_by(ordering),
        template_name='index.html',

    )

def new_post(request):

    if request.method == 'POST':

        post = json.loads(request.raw_post_data)
        form = LeakForm(post)

        if form.is_valid():
            leak = form.save()
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
