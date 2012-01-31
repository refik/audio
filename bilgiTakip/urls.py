from django.conf.urls.defaults import *
from audio.bilgiTakip.views import BilgiDetailView, TipListView, IstatistikView, TemsilciDetailView, TemsilciListView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/teklif'}),
    (r'^(?P<primary_key>\d+)/$', 'audio.bilgiTakip.views.to_new_site'),
    (r'^istatistikler/$', login_required(IstatistikView.as_view())),
    (r'^temsilciler/$', login_required(TemsilciListView.as_view())),
    (r'^temsilci/(?P<pk>\d+)/$', login_required(TemsilciDetailView.as_view())),
)
