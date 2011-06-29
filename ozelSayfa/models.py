from django.db import models
from filebrowser.fields import FileBrowseField

class Sayfa(models.Model):
    isim = models.CharField('Isim',max_length=50)
    def __unicode__(self):
        return u"%s" %(self.isim)

class SayfaMedya(models.Model):
    isim = models.CharField('Isim',max_length=50)
    dosya = FileBrowseField('Medya',max_length=200)
    sayfa = models.ForeignKey(Sayfa)
    yazi = models.CharField('Aciklama',max_length=150)
    def __unicode__(self):
        return self.isim


