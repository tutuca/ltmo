# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap
from django.contrib import admin
from django.views.generic import TemplateView

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
    (r'^l/$','by_tag',{}),
    (r'^l/(?P<tag_name>[\w-]+)$','by_tag',{},'tag'),
    (r'^l/(?P<tag_name>[\w-]+)/(?P<object_id>\d+)$','leak_detail',{},'leak_detail'),
    (r'^tags/','tags',{},'tags'),
    (r'^~(?P<username>\w+)/$','profile_detail', {}, 'author_detail'),
    (r'^in/$', 'login', {}, 'login'),
)
urlpatterns +=patterns('django.contrib.auth.views',
    (r'^out/$', 'logout', {'next_page':'/'}, 'logout'),

)
urlpatterns += patterns('',
    (r'^help/$', TemplateView.as_view(template_name='help.html')),
)
urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^feed/$',LeakFeed()),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /media/*", mimetype="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps})
)
