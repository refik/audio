from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from filebrowser.sites import site
admin.autodiscover()

sitemaps = {
    'duzsayfa': FlatPageSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
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

if settings.LOCAL:
    urlpatterns += patterns('',
        
        url(r'^statik/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.PROJECT_PATH + '/statikTasinmaz',
        }),
        ('^favicon.ico/$', redirect_to, {'url': 'http://s.aucdn.net/resim/favicon.ico'}),
   )
