from django.db import models
from filebrowser.fields import FileBrowseField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.flatpages.models import FlatPage
from audio.urun.models import Kategori, Urun
from audio.dokuman.models import Dokuman

class Link(models.Model):
    sayfa = models.ForeignKey(FlatPage,blank=True, null=True)
    dokuman = models.ForeignKey(Dokuman,blank=True, null=True)
    kategori = models.ForeignKey(Kategori,null=True,blank=True)
    urun = models.ForeignKey(Urun,null=True,blank=True)
    direklink = models.CharField('Direk Link',max_length=200,blank=True)
    dosya = FileBrowseField('Dosya',max_length=200,blank=True)
    def __unicode__(self):
        return self.isim

class Afis(models.Model):
    isim = models.CharField('Isim',max_length=50)
    dosya = FileBrowseField('Medya',max_length=200)
    yazi = models.CharField('Aciklama',max_length=150)
    def __unicode__(self):
        return u"%s" %(self.isim)

class Menu(MPTTModel,Link):
    isim = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childeren')
    def __unicode__(self):
        return u"%s" %(self.isim)


