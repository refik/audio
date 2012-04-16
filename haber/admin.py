from django.contrib import admin
from audio.haber.models import Haber
from audio.settings import STATIC_URL

class HaberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('baslik',)}
    list_display = ['baslik', 'anasayfa']
    list_filter = ['baslik', 'anasayfa']
    fieldsets = (
        ('Haberin Bilgiler', {
            'classes': ('collapse open',),
            'fields': ('baslik', 'slug', 'icerik', 'resim', 'tarih', 'anasayfa', 'detay',),
        }),
    )
    class Media:
        js = [
            '/statik/tinymce/jscripts/tiny_mce/tiny_mce.js',
            STATIC_URL + 'js/tinymce_setup.js',
        ]

admin.site.register(Haber, HaberAdmin)
