from django.conf.urls.defaults import *

urlpatterns = patterns('audio.urun.views',
    (r'^/(?P<urun>[\w\-]+)', 'urun'),
    (r'^ler/(?P<kategori>[\w\-]+)','urunler'),
)
