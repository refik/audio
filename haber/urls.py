from django.conf.urls.defaults import *
from audio.haber.views import HaberView

urlpatterns = patterns('',
    (r'^(?P<slug>[\w\-]+)/$', HaberView.as_view()),
)
