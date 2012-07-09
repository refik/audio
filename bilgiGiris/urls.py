from django.conf.urls.defaults import *

urlpatterns = patterns('audio.bilgiGiris.views',
    (r'^(?P<tip>[\w\-]+)-formu/', 'formIslem'),
)
