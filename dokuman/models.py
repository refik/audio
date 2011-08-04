from django.db import models
from filebrowser.fields import FileBrowseField

class Dokuman(models.Model):
    isim = models.CharField('Isim',max_length=40)
    resim = FileBrowseField('Resim',max_length=200,blank=True,null=True)
    dosya = FileBrowseField('Dosya',max_length=200,null=True)
    slug = models.SlugField()
    urun_sayfa = models.BooleanField('Urun Sayfasinda Gosterilsin')
    class Meta:
        verbose_name_plural = "Dokumanlar"
    def __unicode__(self):
        return u"%s" % (self.isim)

