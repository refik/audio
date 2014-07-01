from audio.calisanProfil.models import CalisanProfil, CalisanGorev
from django.contrib import admin

class ProfilAdmin(admin.ModelAdmin):
    list_display = ['tam_isim','gorev', 'birincil', 'ikincil', 'ucuncul']
    fieldsets = (
        ('Yonetim', {
            'classes': ('collapse open',),
            'fields': ('user',),
        }),
        ('Kullanici Bilgileri', {
            'classes': ('collapse open',),
            'fields' : ('gorev', 'birincil', 'ikincil', 'ucuncul','telefon',),
        }),
        ('Kullanicinin Sorumluluklari', {
            'classes': ('collapse open',),
            'fields' : ('sorumluTip','sorumluSehir','sorumluBolge',),
        }),
    )
    filter_horizontal = ['sorumluTip','sorumluSehir','sorumluBolge']

admin.site.register(CalisanProfil,ProfilAdmin)
admin.site.register(CalisanGorev)
