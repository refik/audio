from audio.urun.models import Urun, Sistem, Kategori, Ozellik, DigerModel
from django.contrib import admin

class UrunDigerInline(admin.StackedInline):
    model = DigerModel
    extra = 0

class UrunAdmin(admin.ModelAdmin):
    list_display = ['isim','yeni']
    inlines = [UrunDigerInline]
    filter_horizontal = ['sistem','ozellik','panel']
    prepopulated_fields = {"slug": ("isim",)}
    fieldsets = (
        ('Urunun Bilgileri', {
            'classes': ('collapse open',),
            'fields': ('isim','slug','kategori','seri',),
        }),
        ('Urunun Tanitimi', {
            'classes': ('collapse open',),
            'fields': ('yeni','resim','resim_yazi','tanitim','ozellik',),
        }),
        ('Urunun Iliskileri', {
            'classes': ('collapse open',),
            'fields': ('sistem','panel',),
        }),
    )
    class Media:
        js = [
            '/statik/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/statik/js/tinymce_setup.js',
        ]



class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('isim',)}
    fieldsets = (
        ('Kategori Ismi', {
            'classes': ('collapse open',),
            'fields': ('isim','slug',),
        }),
    )

class OzellikAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Ozelligin Aciklamasi', {
            'classes': ('collapse open',),
            'fields': ('isim',),
        }),
    )

class SistemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Sistemin Isim ve Kategorisi', {
            'classes': ('collapse open',),
            'fields': ('isim','tip',),
        }),
        ('Sistemin Tanitim Yazisi ve Gosterim Ozellikeri', {
            'classes': ('collapse open',),
            'fields': ('aciklama','resim','sema',),
        }),

    )


admin.site.register(Urun,UrunAdmin)
admin.site.register(Sistem,SistemAdmin)
admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Ozellik,OzellikAdmin)
