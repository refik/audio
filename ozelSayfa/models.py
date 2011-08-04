from django.db import models
from filebrowser.fields import FileBrowseField
from audio.ortakVeri.models import Link

class Sayfa(models.Model):
    isim = models.CharField('Isim',max_length=50)
    def __unicode__(self):
        return u"%s" %(self.isim)

class SayfaLink(Link):
    yazi = models.CharField('Yazili Link Icin',max_length=200,null=True,blank=True)
    gorunum = FileBrowseField('Resimli Link Icin',max_length=200,null=True,blank=True)
    sayfa_ait = models.ForeignKey(Sayfa)
    isim = models.CharField('Isim',max_length=200)

