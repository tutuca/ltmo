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
    (r'^leak/$','leak_new',{},'leak_new'),
    (r'^leak/(?P<object_id>\d+)$','leak_detail',{},'leak_detail'),
    (r'^raw_leak/(?P<object_id>\d+)$','render_leak',{},'render_leak'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^feed/$',LeakFeed()),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /media/*", mimetype="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps})

)

urlpatterns += patterns(
    'piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)
      
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT})
    )
    
