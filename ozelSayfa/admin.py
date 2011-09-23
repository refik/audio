from audio.ozelSayfa.models import Sayfa, SayfaLink
from django.contrib import admin, databrowse

class SayfaLinkInline(admin.StackedInline):
    model = SayfaLink
    extra = 0

class SayfaAdmin(admin.ModelAdmin):
    inlines = [ SayfaLinkInline ]
    fieldsets = (
        ('Sayfa Ismi', {
            'classes': ('collapse open',),
            'fields': ('isim',),
        }),
    )

admin.site.register(Sayfa,SayfaAdmin)
