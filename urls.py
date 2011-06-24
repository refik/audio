from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^form/', include('audio.bilgiGiris.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^databrowse/(.*)', databrowse.site.root),
    
    (r'^$', include('audio.ozelSayfa.urls')),
)
