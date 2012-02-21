from django.conf.urls.defaults import *
from django.contrib.auth.views import logout, password_change, password_change_done

urlpatterns = patterns('audio.ozelSayfa.views',
    (r'^$', 'anasayfa'),
    (r'^logout/',logout),
    (r'^password_change/', password_change),
    (r'password/done/$', password_change_done) 
) 
