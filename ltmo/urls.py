# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap
from django.contrib import admin

from leaks.feeds import LeakFeed
from leaks.models import Leak

info_dict = {
    'queryset': Leak.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'leaks': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('leaks.views',
    (r'^$','index',{},'index'),
    (r'^new/$','edit',{},'new'),
    (r'^edit/(?P<id>\d+)$','edit',{},'edit'),
    (r'^l/$','by_tag',{}),
    (r'^leak/(?P<tag_name>\D+)$','by_tag',{},'by_tag'),
    (r'^leak/(?P<id>\d+)$','leak_detail',{},'leak_detail'),
    (r'^tags/','tags',{},'tags'),
    (r'^~$', 'user_profile', {}, 'author'),
    (r'^~(?P<username>\w+)/$','user_profile', {}, 'author_detail'),
    (r'^register$','register',{},'register'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'login$', 'login', {'template_name':'login.html'}, 'login'),
    (r'^logout$', 'logout', {'next_page':'/'}, 'logout'),
)

urlpatterns += patterns('',
    url('', include('social.apps.django_app.urls', namespace='social'))
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
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.UPLOAD_DIR,
        }),
   )
