# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf import settings
from django.http import HttpResponse
from django.views.static import serve
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.views import login, logout
from django.contrib import admin

from ltmo.feeds import LeakFeed
from ltmo.models import Leak
from ltmo import views as ltmo_views

admin.autodiscover()

info_dict = {
    'queryset': Leak.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'leaks': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = [
    url(r'^$', ltmo_views.index, {}, name='index'),
    url(r'^new/$', ltmo_views.edit,{}, name='new'),
    url(r'^edit/(?P<id>\d+)$', ltmo_views.edit,{}, name='edit'),
    url(r'^l/$', ltmo_views.by_tag,{}),
    url(r'^leak/(?P<tag_name>\D+)$', ltmo_views.by_tag,{}, name='by_tag'),
    url(r'^leak/(?P<id>\d+)$', ltmo_views.leak_detail,{}, name='leak_detail'),
    url(r'^tags/', ltmo_views.tags,{}, name='tags'),
    url(r'^~$', ltmo_views.user_profile, {}, name='author'),
    url(r'^~(?P<username>\w+)/$', ltmo_views.user_profile, {}, name='author_detail'),
    url(r'^register$', ltmo_views.register,{}, name='register'),
]

urlpatterns += [
    url(r'login$', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout$', logout, {'next_page':'/'}, name='logout'),
]

urlpatterns += [
    url('', include('social.apps.django_app.urls', namespace='social'))
]
urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/$',LeakFeed()),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /media/*", mimetype="text/plain")),
    url(r'^sitemap\.xml$', sitemap, 
        {'sitemaps': sitemaps})
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.UPLOAD_DIR,
        }),
   ]
