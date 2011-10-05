from audio.ortakVeri.models import Afis, Menu
from django.contrib import admin, sites, comments
from feincms.admin.tree_editor import TreeEditor
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = [
            '/statik/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/statik/js/tinymce_setup.js',
        ]

class MenuAdmin(TreeEditor, admin.ModelAdmin):
    fieldsets = (
        ('Menu Bilgileri', {
            'classes': ('collapse open',),
            'fields': ('isim', 'parent',),
        }),
        ('Menunun Yonlendirecegi Yer', {
            'classes': ('collapse open',),
            'fields' : ('sayfa', 'urun','kategori','dokuman','dosya','direklink',),
        }),
    )

class AfisAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Afis Bilgileri', {
            'classes': ('collapse open',),
            'fields': ('yazi','resim',),
        }),
    )


admin.site.register(Afis, AfisAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.unregister(sites.models.Site)
#admin.site.unregister(comments.models.Comment)


