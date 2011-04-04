# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import list_detail, simple
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from tagging.models import Tag

from ltmo.forms import LeakForm
from ltmo.models import Leak


def index(request, object_id=None):
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
            messages.success(request, 'ha derramado correctamente chamigo.')
            return redirect(next)
            
    return list_detail.object_list(
        request,
        queryset,
        template_name='index.html',
        extra_context={
            'form': form,
        }
    )

def leak_detail(request, tag_name, object_id):
    queryset = Leak.objects.all()
    form = LeakForm(initial={'tags':tag_name})
    leak = get_object_or_404(Leak, pk=object_id)
    
    if request.is_ajax():
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
        form = LeakForm(request.POST, instance=leak)
        if form.is_valid():
            leak = form.save()
            messages.success(request, 'actualizaste el #%s' %(object_id))
            return redirect(next)
            
    return list_detail.object_detail(
        request,
        queryset.filter(tags__icontains=tag_name),
        leak.pk,
        template_name='detail.html',
        extra_context={
            'form': form,
            'tag': tag_name
        }
    )
        
def by_tag(request, tag_name=None):
    queryset = Leak.objects.all().order_by('tags')
    form = LeakForm()

    if tag_name:
        queryset = queryset.filter(tags__icontains=tag_name)

    return list_detail.object_list(
        request,
        queryset,
        template_name='tags.html',
        extra_context={
            'form': form,
            'tag_name': tag_name,
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

def profile_detail(request, username):
    queryset = Leak.objects.filter(author__icontains=username).order_by('-created')
    form = LeakForm()
    try:
        author = User.objects.get(username__icontains=username)
    except :
        author = None

    return list_detail.object_list(
        request,
        queryset,
        template_name='profile.html',
        extra_context={
            'author':author,
            'form':form,
            'is_me':request.user.username == 'username',
        }
    )

def login(request):
    if request.method == 'POST':
        from django.contrib.auth import authenticate, login
        username = request.POST.get('username', 'None')
        password = request.POST.get('password', 'None')
        user = authenticate(username=username, password=password)
        next = request.POST.get('next')
        message = ''
        if user is not None:
            if user.is_active:
                login(request, user)
                message = "bienvenido"
                messages.success(request, 'bienvenido %s' %(user, ))
                
            else:
                messages.warning(request, 'tu cuenta fue deshabilitada')
        else:
            messages.error(request, 'nombre de usuario y contraseña incorrectos')
            
        return HttpResponse(
            json.dumps({
                'next': next,
            }),
            
            mimetype="application/json"
        )

