from django.conf.urls.defaults import *
from django.contrib.auth.views import logout, password_change, password_change_done

urlpatterns = patterns('audio.ozelSayfa.views',
    (r'^$', 'anasayfa'),
    (r'^logout/','logout_view'),
    (r'^sifre-degistir/', password_change),
    (r'^ozel-giris/(?P<username>[\w\-]+)/$', 'special_entrance'),
    (r'^password/done/$', password_change_done),
    (r'^stand-secimi/','stand_secimi'),
    (r'^numune-panosu/','numune_panosu'),
    (r'^baglanti-semalari/','baglanti_semalari'),
)
