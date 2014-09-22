from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, TemplateView
from audio.teklif.views import OfferView, DoneView, NewView, TeklifDosyaView, YonetimView
from audio.teklif.models import Teklif

urlpatterns = patterns('audio.teklif.views',
    (r'^$', never_cache(login_required(OfferView.as_view()))),
    (r'^(?P<pk>\d+)/$', never_cache(login_required(OfferView.as_view()))),
    (r'^sorumlu/(?P<pk>\d+)/$', never_cache(login_required(DetailView.as_view(template_name = 'sorumlu.html',
                                                                              context_object_name = 'teklif',
                                                                              model = Teklif)))),
    (r'^yapildi/(?P<pk>\d+)/$', never_cache(login_required(DetailView.as_view(template_name = 'yapildi.html',
                                                                              context_object_name = 'teklif',
                                                                              model = Teklif)))),
    (r'^yenile/(?P<pk>\d+)/$', never_cache(login_required(DetailView.as_view(template_name = 'offer.html',
                                                                              context_object_name = 'offer',
                                                                              model = Teklif)))),
    (r'^yeni/(?P<pk>\d+)/$', never_cache(login_required(NewView.as_view()))),
    (r'^iscilik/(?P<pk>\d+)/$', never_cache(login_required(TeklifDosyaView.as_view()))),
    #(r'^iscilik-tutar/$', never_cache(login_required(IscilikTutarView.as_view()))),
    (r'^form/$', never_cache(login_required(DoneView.as_view()))),
    (r'^success/$', TemplateView.as_view(template_name='success.html')),
    (r'^yonetim/$', never_cache(login_required(YonetimView.as_view()))),
    (r'^yonetim/degistir/$', 'yonetim_degistir'),
    (r'^yapildi/$', 'yapildi_yolla'),
    (r'^sifremi-unuttum/$', 'sifremi_unuttum'),
)
