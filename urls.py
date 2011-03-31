from django.conf import settings
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap
from django.contrib import admin

from ltmo.feeds import LeakFeed
from ltmo.models import Leak

admin.autodiscover()

info_dict = {
    'queryset': Leak.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'leaks': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('ltmo.views',
    (r'^$','index',{},'index'),
    (r'^leak/$','index',{},'leak_new'),
    (r'^(?P<object_id>\d+)$','leak_detail',{},'leak_detail'),
    (r'^(?P<tag>\w+)$','index',{},'list_by_tag'),
    (r'^~(?P<author>\w+)$','index',{},'list_by_author'),
    (r'^tags','tags',{},'tags'),

)
urlpatterns += patterns('django.views.generic',
    (r'^help/$', 'simple.direct_to_template', {'template': 'help.html', 'extra_context':{'title':'Ayuuuudaaaa'},}),
)
urlpatterns += patterns('',

    (r'^admin/', include(admin.site.urls)),
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
    
