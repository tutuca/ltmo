from django.conf.urls.defaults import *
from django.conf import settings
from ltmo.feeds import LeakFeed
from ltmo.models import LTMOSitemap

sitemaps = {
    'blog': LTMOSitemap,
}

urlpatterns = patterns('',
    (r'^$','views.index',{},'index'),
    (r'^leak/(?P<object_id>\d+)$','views.leak_detail',{},'leak_detail'),
    (r'^derramo/','views.new_post',{},' new_post'),
    (r'^feed/$',LeakFeed()),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps})

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT})
    )
    
