from audio.haber.models import Haber
from django.contrib import admin

class HaberAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("baslik",)}


admin.site.register(Haber, HaberAdmin)
