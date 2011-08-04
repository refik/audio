from audio.urun.models import Urun, Sistem, YeniUrun, Kategori, Ozellik, DigerModel
from django.contrib import admin

class UrunDigerInline(admin.StackedInline):
    model = DigerModel
    extra = 0

class UrunAdmin(admin.ModelAdmin):
    inlines = [UrunDigerInline]

admin.site.register(Urun,UrunAdmin)
admin.site.register(Sistem)
admin.site.register(YeniUrun)
admin.site.register(Kategori)
admin.site.register(Ozellik)
