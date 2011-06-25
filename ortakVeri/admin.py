from audio.ortakVeri.models import Afis, Menu
from django.contrib import admin
from feincms.admin.tree_editor import TreeEditor
#from mptt.admin import MPTTModelAdmin

class MenuAdmin(TreeEditor, admin.ModelAdmin):
    pass

admin.site.register(Afis)
admin.site.register(Menu, MenuAdmin)

