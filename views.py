from django.views.generic import list_detail, simple
from ltmo.models import Leak
from django.conf import settings
from django.utils import simplejson as json

def index(request):
    author = request.GET.get('author',None)
    tag = request.GET.get('tag',None)
    queryset = Leak.objects.all().order_by('-created')
    if author:
        queryset = queryset.filter(author = author)
    if tag:
        queryset = queryset.filter(tags__icontains=tag)

    return list_detail.object_list(
        request,
        queryset,
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
