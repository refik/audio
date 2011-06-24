from django.db import models
from filebrowser.fields import FileBrowseField
from datetime import datetime

class Haber(models.Model):
    baslik = models.CharField('Baslik',max_length=40)
    icerik = models.TextField('Haber')
    resim = FileBrowseField('Resim',max_length=200)
    meta = models.CharField('Meta etiketleri',max_length=100)
    slug = models.SlugField()
    tarih = models.DateTimeField('Yayinlanma Tarihi',default = datetime.now())
    class Meta:
        verbose_name_plural = "Haberler"
    def __unicode__(self):
        return u"%s" % (self.baslik)

