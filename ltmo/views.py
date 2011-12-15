# -*- coding: utf-8 -*-


from django.conf import settings
from django.core.mail import send_mail
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.contrib import messages, auth 
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from tagging.models import Tag
from django.contrib.auth.decorators import login_required
from ltmo.forms import LeakForm, RegisterForm
from ltmo.models import Leak, Attach

def index(request, object_id=None):
    try:
        queryset = Leak.objects.all().order_by('-created')
        latest = queryset.latest('created')
    
    except Leak.DoesNotExist, e:
        queryset = None
        latest = None
    return render(
        request,
        'detail.html',
        {
            'object_list':queryset,
            'object':latest,
        }
    )

@login_required()
def edit(request, id=None):
    AttachFormset = inlineformset_factory(Leak, Attach)
    if id:
        leak = get_object_or_404(Leak, pk=id)
        form = LeakForm(instance=leak)
    else:
        form = LeakForm(initial={'author':request.user})
        leak = None
    if request.method == 'POST':
        next = request.POST['next']
        form = LeakForm(request.POST, instance=leak)
        if form.is_valid():
            leak = form.save()
            return redirect(leak.get_absolute_url())
            
    return render(
        request,
        'leak_form.html',
        {
            'form': form,
        }
    )


def leak_detail(request, id=None):
    queryset = Leak.objects.all()
    leak = get_object_or_404(Leak, pk=id)

    return render(
        request,
        'detail.html',
        {
            'object_list': queryset,
            'object': leak,
        }
    )
        
def by_tag(request, tag_name=None):
    queryset = Leak.objects.all().order_by('tags')
    form = LeakForm()

    if tag_name:
        queryset = queryset.filter(tags__icontains=tag_name)

    return render(
        request,
        'tags.html',
        {
            'object_list': queryset,
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

    try:
        author = User.objects.get(username__icontains=username)
    except :
        author = None

    return render(
        request,
        'profile.html',
        {
            'object_list': queryset,
            'author':author,
            'is_me':request.user.username == 'username',
        }
    )

def register(request,):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and not form.data['honeypot']:
            message = 'nombre: %s . email: %s' %(form.data['username'], form.data['email'])
            send_mail(
                'Pedido de cuenta',
                message,
                form.data['email'],
                [x[1] for x in settings.ADMINS]
            )
            return redirect('/')

    return render(
        request, 
        'register.html',
        {
            'form': form,
        }
    )

