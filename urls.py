from django.conf import settings
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap


from ltmo.feeds import LeakFeed
from ltmo.models import Leak

info_dict = {
    'queryset': Leak.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'leaks': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('',
    (r'^$','views.index',{},'index'),
    (r'^leak/(?P<object_id>\d+)$','views.leak_detail',{},'leak_detail'),
    (r'^derramo[/]{0,1}','views.new_post',{},' new_post'),
    (r'^feed/$',LeakFeed()),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /media/*", mimetype="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps})

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT})
    )
    
