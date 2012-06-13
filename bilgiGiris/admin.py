from audio.bilgiGiris.models import Bilgi, Tip, Sehir, Ilce
from django.contrib import admin

class BilgiAdmin(admin.ModelAdmin):
    search_fields = ['isim']
    list_display = ['isim', 'tip','tarih']
    fieldsets = (
        ('Gonderenin Bilgileri', {
            'classes': ('collapse open',),
            'fields': ('isim', 'telefon', 'firma', 'email','sehir','ilce','adres','no'),
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
admin.site.register(Ilce)
admin.site.register(Sehir)
admin.site.register(Tip)
