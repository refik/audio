from audio.teklif.models import Teklif, TeklifYorum, Durum, Rakip, Sebep
from django.contrib import admin

admin.site.register(Rakip)
admin.site.register(Sebep)
admin.site.register(Durum)
admin.site.register(TeklifYorum)
admin.site.register(Teklif)
