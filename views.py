from django.conf import settings
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import list_detail, simple
from django.http import HttpResponse
from django.shortcuts import redirect
from tagging.models import Tag

from ltmo.forms import LeakForm
from ltmo.models import Leak


def index(request, tag=None, author=None):
    queryset = Leak.objects.all().order_by('-created')
    form = LeakForm()

    if request.method == 'POST':

        try:
            data = json.loads(request.raw_post_data) 
        except ValueError:
            data = request.POST
        
        form = LeakForm(data)

        if form.is_valid():
            next = request.POST['next']
            leak = form.save()
            messages.success(request, 'Ha derramado correctamente chamigo.')
            return redirect(next)
            
    return list_detail.object_list(
        request,
        queryset,
        template_name='index.html',
        extra_context={
            'form': form,
        }
    )
def by_tag(request, tag_name=None):
    queryset = Tag.objects.all()
    form = LeakForm()
    title = 'Derrames por etiqueta'
    
    return list_detail.object_list(
        request,
        queryset,
        template_name='tags.html',
        extra_context={
            'form': form,
            'tag_name': tag_name,
        }
    )
def leak_detail(request, object_id):
    form = LeakForm()
    if request.is_ajax():
        leak = Leak.objects.get(id=object_id)
        return HttpResponse(
            json.dumps({
                'title':leak.title,
                'author':leak.author,
                'description':leak.description,
                'tags': leak.tags
            }),
            
            mimetype="application/json"
        )

    if request.method == 'POST':
        next = request.POST['next']
        form = LeakForm(request.POST, instance=Leak.objects.get(id=object_id))
        if form.is_valid():
            leak = form.save()
            messages.success(request, 'Actualizaste el #%s' %(object_id))
            return redirect(next)
            

    queryset = Leak.objects.all()
    return list_detail.object_detail(
        request,
        queryset,
        object_id,
        template_name='detail.html',
        extra_context={
            'form': form,
        }
    )

def tags(request):
    queryset = Tag.objects.all()
    tag_name = request.GET.get('tag_name')
    if tag_name:
        queryset = queryset.filter(name__istartswith=tag_name)
    return HttpResponse(
        json.dumps([x.name for x in queryset]), 
        mimetype="application/json"
    )

