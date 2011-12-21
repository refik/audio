from django.conf.urls.defaults import *
from audio.bilgiTakip.views import BilgiDetailView, TipListView, IstatistikView, TemsilciDetailView, TemsilciListView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

urlpatterns = patterns('',
    (r'^$', never_cache(login_required(TipListView.as_view()))),
    (r'^(?P<pk>\d+)/$', login_required(BilgiDetailView.as_view())),
    (r'^istatistikler/$', login_required(IstatistikView.as_view())),
    (r'^temsilciler/$', login_required(TemsilciListView.as_view())),
    (r'^temsilci/(?P<pk>\d+)/$', login_required(TemsilciDetailView.as_view())),
)
