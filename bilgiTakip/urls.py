from django.conf.urls.defaults import *
from audio.bilgiTakip.views import BilgiDetailView, TipListView, IstatistikView, TemsilciDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    (r'^$', login_required(TipListView.as_view())),
    (r'^(?P<pk>\d+)/$', login_required(BilgiDetailView.as_view())),
    (r'^istatistikler/$', login_required(IstatistikView.as_view())),
    (r'^temsilci/(?P<pk>\d+)/$', login_required(TemsilciDetailView.as_view())),
)
