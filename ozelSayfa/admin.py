from audio.ozelSayfa.models import Sayfa, SayfaMedya 
from django.contrib import admin, databrowse

class SayfaMedyaInline(admin.TabularInline):
    model = SayfaMedya
    extra = 2

class SayfaAdmin(admin.ModelAdmin):
    inlines = [ SayfaMedyaInline ]

admin.site.register(Sayfa,SayfaAdmin)
