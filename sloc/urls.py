from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('horai.sloc.views',
    (r'^/$', 'index'),

    (r'^/segment/(?P<segment_id>\d+)/detail$', 'segment_detail'),
    (r'^/segment/(?P<segment_id>\d+)/detail/segment.csv$', 'segment_detail_csv'),

    (r'^/language/(?P<language_id>\d+)/detail$', 'language_detail'),
    (r'^/language/(?P<language_id>\d+)/detail/language.csv$', 'language_detail_csv'),

    (r'^/add$', 'sloc_add'),
)
