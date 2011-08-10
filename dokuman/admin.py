from audio.dokuman.models import Dokuman
from django.contrib import admin

class DokumanAdmin(admin.ModelAdmin):
    list_display = ['isim','urun_sayfa']
    prepopulated_fields = {"slug": ("isim",)}
    fieldsets = (
        ('Dokuman Ismi', {
            'classes': ('collapse open',),
            'fields': ('isim', 'slug',),
        }),
        ('Dosya', {
            'classes': ('collapse open',),
            'fields' : ('dosya',),
        }),
        ('Urun Sayfasinda Gosterim', {
            'classes': ('collapse open',),
            'fields' : ('resim','urun_sayfa',),
        }),
    )

admin.site.register(Dokuman,DokumanAdmin)

