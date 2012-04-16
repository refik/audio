from django.db import models
from filebrowser.fields import FileBrowseField
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from audio.ortakVeri.sprite import sprite_generator
import os

class Haber(models.Model):
    baslik = models.CharField('Baslik',max_length=22)
    icerik = models.CharField('Icerik Yazisi', max_length=60)
    resim = FileBrowseField('Resim',max_length=200)
    detay = models.TextField('Haberin Detaylari', blank=True, null=True)
    anasayfa = models.BooleanField('Anasayfada gosterilsin')
    tarih = models.DateTimeField()
    slug =  models.SlugField('Duzlestirilmis Isim')

    class Meta:
        verbose_name_plural = "Haberler"
        ordering = ['tarih']

    def __unicode__(self):
        return unicode(self.baslik)

    def get_absolute_url(self):
        return 'http://www.audio.com.tr/haber/' + self.slug

@receiver(post_save, sender=Haber)
def haber_sprite(sender, **kwargs):
    pic_haber = [haber.resim for haber in Haber.objects.filter(anasayfa=True)]
    pic_ver = [pic.version_generate('haber_ufak') for pic in pic_haber]
    sprite_generator('news', pic_ver)
