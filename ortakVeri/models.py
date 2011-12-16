from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey
from filebrowser.fields import FileBrowseField
from storages.backends.mosso import CloudFilesStorage
from audio.urun.models import Kategori, Urun
from audio.dokuman.models import Dokuman



class Link(models.Model):
    sayfa = models.ForeignKey(FlatPage,blank=True, null=True)
    dokuman = models.ForeignKey(Dokuman,blank=True, null=True)
    kategori = models.ForeignKey(Kategori,null=True,blank=True)
    urun = models.ForeignKey(Urun,null=True,blank=True)
    direklink = models.CharField('Direk Link',max_length=200,blank=True,null=True)
    dosya = FileBrowseField('Dosya',max_length=200,blank=True,null=True)
    class Meta:
        verbose_name_plural = 'Linkler'
    def __unicode__(self):
        try:
            return unicode(self.isim)
        except:
            return ""

class Afis(models.Model):
    resim = FileBrowseField('Resim',max_length=200,help_text='Resmin boyutu tam olarak 952x217 pixel olmalidir')
    yazi = models.CharField('Aciklama',max_length=150)
    class Meta:
        verbose_name_plural = 'Afisler'
    def __unicode__(self):
        return unicode(self.yazi)

class Menu(MPTTModel,Link):
    isim = models.CharField('Isim',max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childeren')
    class Meta:
        verbose_name_plural = 'Menuler'
    def __unicode__(self):
        return unicode(self.isim)


