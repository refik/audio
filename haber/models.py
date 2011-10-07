from django.db import models
from filebrowser.fields import FileBrowseField
from datetime import datetime

class Haber(models.Model):
    baslik = models.CharField('Baslik',max_length=32)
    icerik = models.CharField('Icerik Yazisi', max_length=60)
    resim = FileBrowseField('Resim',max_length=200)
    class Meta:
        verbose_name_plural = "Haberler"
    def __unicode__(self):
        return unicode(self.baslik)

