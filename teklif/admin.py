from audio.teklif.models import Teklif, Durum, Rakip, Sebep, Yapildi
from django.contrib import admin

admin.site.register(Yapildi)
admin.site.register(Rakip)
admin.site.register(Sebep)
admin.site.register(Durum)
admin.site.register(Teklif)
