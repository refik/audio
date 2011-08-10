from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^urun', include('audio.urun.urls')),
    (r'^form/', include('audio.bilgiGiris.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^takip/', include('audio.bilgiTakip.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^dokuman/', include('audio.dokuman.urls')),
    (r'^', include('audio.calisanProfil.urls')),
    (r'^', include('audio.bilgiGiris.urls')), 
    (r'^', include('audio.ozelSayfa.urls')),
)
