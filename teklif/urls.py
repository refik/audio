from django.conf.urls.defaults import *

urlpatterns = patterns('audio.teklif.views',
    (r'^yapildi$', 'yapildi_yolla'),
)
