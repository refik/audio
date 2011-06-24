from django.db import models
from datetime import datetime

class Tip(models.Model):
    isim = models.CharField('Alan',max_length = 200)
    def __unicode__(self):
        return self.isim

class Sehir(models.Model):
    isim = models.CharField('Sehir',max_length = 200)
    def __unicode__(self):
        return self.isim

class Bilgi(models.Model):
    isim = models.CharField('Isim', max_length = 50)
    sehir = models.ForeignKey(Sehir)
    telefon = models.CharField('Telefon', max_length = 50)
    email = models.EmailField('Email')
    firma = models.CharField('Firma', max_length = 200)
    mesaj = models.TextField('Mesaj')
    tip = models.ForeignKey(Tip)
    tarih = models.DateTimeField("Giris Tarihi", default = datetime.now(),editable=False)
    def __unicode__(self):
        return self.isim


