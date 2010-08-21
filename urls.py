from django.conf.urls.defaults import *

urlpatterns = patterns('views',
    (r'^$','index',{},'index'),
    (r'^derramo/','new_post',{},' new_post'),
)
