from django.conf.urls.defaults import *
from audio.bilgiTakip.views import TakipDetailView

urlpatterns = patterns('audio.bilgiTakip.views',
    (r'^$', 'goster'),
    (r'^(?P<pk>\d+)', TakipDetailView.as_view()),
)
