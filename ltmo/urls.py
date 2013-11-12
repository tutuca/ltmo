# -*- coding: utf-8 -*-


from django.conf.urls.defaults import patterns, include
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
    (r'^new/$','edit',{},'new'),
    (r'^edit/(?P<id>\d+)$','edit',{},'edit'),
    (r'^l/$','by_tag',{}),
    (r'^leak/(?P<tag_name>\D+)$','by_tag',{},'by_tag'),
    (r'^leak/(?P<id>\d+)$','leak_detail',{},'leak_detail'),
    (r'^tags/','tags',{},'tags'),
    (r'^~(?P<username>\w+)/$','profile_detail', {}, 'author_detail'),
    (r'^register$','register',{},'register'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'login$', 'login', {'template_name':'login.html'}, 'login'),
    (r'^logout$', 'logout', {'next_page':'/'}, 'logout'),
)
urlpatterns += patterns('',
    (r'', include('social_auth.urls')))
urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^feed/$',LeakFeed()),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /media/*", mimetype="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps})
)
