from django.db import models
from filebrowser.fields import FileBrowseField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.flatpages.models import FlatPage

class Afis(models.Model):
    isim = models.CharField('Isim',max_length=50)
    dosya = FileBrowseField('Medya',max_length=200)
    yazi = models.CharField('Aciklama',max_length=150)
    def __unicode__(self):
        return u"%s" %(self.isim)

class Menu(MPTTModel):
    isim = models.CharField('Isim',max_length=50)
    sayfa = models.ForeignKey(FlatPage,blank=True, null=True)
    dosya = FileBrowseField('Dosya',max_length=200,blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childeren')

    def __unicode__(self):
        return u"%s" %(self.isim)
