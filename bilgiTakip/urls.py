from django.conf.urls.defaults import *
from audio.bilgiTakip.views import BilgiDetailView, TipListView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    (r'^$', login_required(TipListView.as_view())),
    (r'^(?P<pk>\d+)/$', login_required(BilgiDetailView.as_view())),
)
