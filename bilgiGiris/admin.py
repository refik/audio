from audio.bilgiGiris.models import Bilgi, Tip, Sehir
from django.contrib import admin

class BilgiAdmin(admin.ModelAdmin):
    list_display = ['isim', 'tip','tarih']
    fieldsets = (
        ('Gonderenin Bilgileri', {
            'classes': ('collapse open',),
            'fields': ('isim', 'telefon', 'firma', 'email','sehir',),
        }),
        ('Istek', {
            'classes': ('collapse open',),
            'fields' : ('tip', 'mesaj',),
        }),
        ('Yonetim', {
            'classes': ('collapse open',),
            'fields' : ('sorumlu',),
        }),
    )
    filter_horizontal = ['sorumlu']

admin.site.register(Bilgi, BilgiAdmin)
