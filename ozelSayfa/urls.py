from django.conf.urls.defaults import *

urlpatterns = patterns('audio.ozelSayfa.views',
    (r'^$', 'anasayfa'),
    (r'^logout/','logout_view'),
#    (r'^kalite-belgelerimiz/','kaliteBelgelerimiz'),
)
