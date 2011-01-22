from django.conf import settings
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.views.generic import list_detail, simple

from ltmo.forms import LeakForm
from ltmo.models import Leak


def index(request):
    author = request.GET.get('author', None)
    tag = request.GET.get('tag', None)
    queryset = Leak.objects.all().order_by('-created')
    form = LeakForm()
    if author:
        queryset = queryset.filter(author__icontains=author)
        try:
            author = User.objects.get(username__icontains=author)
        except User.DoesNotExist:
            author = None
    if tag:
        queryset = queryset.filter(tags__icontains=tag)

    if request.method == 'POST':
        post = json.loads(request.raw_post_data)
        form = LeakForm(post)
        if form.is_valid():
            leak = form.save()
        return simple.direct_to_template(
            request,
            'success.json',
            mimetype='application/json',
            extra_context={
                'form': form,
            }
        )
    return list_detail.object_list(
        request,
        queryset,
        template_name='index.html',
        extra_context={
            'author': author,
            'tag': tag,
            'form': form,
        }
    )



def leak_detail(request, object_id):
    if request.method == 'POST':
        post = json.loads(request.raw_post_data)
        form = LeakForm(post, instance=Leak.objects.get(id=object_id))

        if form.is_valid():
            leak = form.save()
        return simple.direct_to_template(
            request,
            'success.json',
            mimetype='application/json',
            extra_context={
                'form': form,
            }
        )

    queryset = Leak.objects.all()
    return list_detail.object_detail(
        request,
        queryset,
        object_id,
        template_name='detail.html',
    )
