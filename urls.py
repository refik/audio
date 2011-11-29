from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from filebrowser.sites import site
admin.autodiscover()

sitemaps = {
    'duzsayfa': FlatPageSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    (r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '/statik/resim/favicon.ico'}),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^urun', include('audio.urun.urls')),
    (r'^form/', include('audio.bilgiGiris.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^takip/', include('audio.bilgiTakip.urls')),
    (r'^teklif/', include('audio.teklif.urls')),
    (r'^dokuman/', include('audio.dokuman.urls')),
    (r'^accounts/login/$','django.contrib.auth.views.login'),
    (r'^', include('audio.urun.urls')),
    (r'^', include('audio.calisanProfil.urls')),
    (r'^', include('audio.bilgiGiris.urls')), 
    (r'^', include('audio.ozelSayfa.urls')),
)
