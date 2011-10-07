from audio.haber.models import Haber
from django.contrib import admin

class HaberAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Haberin Bilgiler', {
            'classes': ('collapse open',),
            'fields': ('baslik','icerik','resim',),
        }),
    )

admin.site.register(Haber, HaberAdmin)
