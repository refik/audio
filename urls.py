from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from filebrowser.sites import site
from audio.teklif.views import OtomatikTeklif
from audio.dokuman.models import Dokuman
from audio.urun.models import Urun, Kategori
from audio.ortakVeri.sitemap import EkstraSitemap
admin.autodiscover()

urun_dict = {
    'queryset': Urun.objects.all()
}

dokuman_dict = {
    'queryset': Dokuman.objects.all()
}    

kategori_dict = {
    'queryset': Kategori.objects.all()
}

sitemaps = {
    'duzsayfa': FlatPageSitemap,
    'kategori': GenericSitemap(kategori_dict),
    'urun': GenericSitemap(urun_dict),
    'dokuman': GenericSitemap(dokuman_dict),
    'diger': EkstraSitemap
}

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^site_media/', redirect_to, {'url': None}),
    (r'^urunler/urun/', redirect_to, {'url': None}),
    (r'^turkish/', redirect_to, {'url': None}),
    (r'^english/', redirect_to, {'url': None}),
    (r'^urun', include('audio.urun.urls')),
    (r'^form/', include('audio.bilgiGiris.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^takip/', include('audio.bilgiTakip.urls')),
    (r'^teklif/', include('audio.teklif.urls')),
    (r'^teklif-istiyorum/', OtomatikTeklif.as_view()),
    (r'^dokuman/', include('audio.dokuman.urls')),
    (r'^accounts/login/$','django.contrib.auth.views.login'),
    (r'^', include('audio.urun.urls')),
    (r'^', include('audio.calisanProfil.urls')),
    (r'^', include('audio.bilgiGiris.urls')), 
    (r'^', include('audio.ozelSayfa.urls')),
)

if settings.LOCAL:
    urlpatterns += patterns('',
         url(r'^static-development/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.PROJECT_PATH + '/statik',
        }),
        url(r'^statik/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.PROJECT_PATH + '/statikTasinmaz',
        }),
        ('^favicon.ico/$', redirect_to, {'url': 'http://s.aucdn.net/resim/favicon.ico'}),
   )
