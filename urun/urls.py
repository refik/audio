from django.conf.urls.defaults import *

urlpatterns = patterns('audio.urun.views',
    (r'^sistemler/$', 'sistem'),
    (r'^/(?P<urun>[\w\-]+)/$', 'urun'),
    (r'^ler/(?P<kategori>[\w\-]+)/$','urunler'),
)
