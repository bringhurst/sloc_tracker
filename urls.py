from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^sloc', include('horai.sloc.urls')),
    (r'^sloc/admin/', include(admin.site.urls)),
)
