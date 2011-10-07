from django.conf.urls.defaults import *

urlpatterns = patterns('audio.dokuman.views',
    (r'^(?P<isim>[\w\-\.]+)/', 'dokuman'),
)
