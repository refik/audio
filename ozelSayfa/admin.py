from audio.ozelSayfa.models import Sayfa, SayfaLink
from django.contrib import admin, databrowse

class SayfaLinkInline(admin.StackedInline):
    model = SayfaLink
    extra = 0

class SayfaAdmin(admin.ModelAdmin):
    inlines = [ SayfaLinkInline ]

admin.site.register(Sayfa,SayfaAdmin)
