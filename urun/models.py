# coding: utf-8
from django.db import models
from filebrowser.fields import FileBrowseField

SERI=(
     ("konsept","Konsept"),
     ("basic","Basic"),
     )

TIP =(
     ("goruntulu","Goruntulu"),
     ("sesli","Sesli"),
     )

class Sistem(models.Model):
    isim = models.CharField("Isim",max_length=200)
    tip = models.CharField("Tip", max_length = 50, choices =TIP)
    aciklama = models.TextField()
    tanitim = FileBrowseField('Tanitim Brosuru',max_length=50)
    class Meta: 
        verbose_name_plural = "Sistemler"
    def __unicode__(self):
        return self.isim

class Ozellik(models.Model):
    isim = models.CharField("Isim", max_length = 50)
    class Meta:
        verbose_name_plural = "Ozellikler"
    def __unicode__(self):
        return self.isim

class Kategori(models.Model):
    isim = models.CharField("Isim", max_length=50)
    slug = models.SlugField("Kategori", max_length = 50)
    def __unicode__(self):
        return self.isim

class Urun(models.Model):
    isim = models.CharField("Isim", max_length=50)
    resim = FileBrowseField('Urunun Resmi', max_length=200) 
    sistem = models.ManyToManyField(Sistem)
    kategori = models.ForeignKey(Kategori, related_name="UrunKategori", verbose_name="Kategori")
    seri = models.CharField("Seri",max_length=10,choices=SERI)
    tanitim = models.TextField("Tanitim Metni")
    ozellik = models.ManyToManyField(Ozellik, blank= True, related_name = "UrunOzellikler")
    slug = models.SlugField()
    panel = models.ManyToManyField('self')
    class Meta:
        verbose_name_plural = "Urunler"
    def __unicode__(self):
        return self.isim

class DigerModel(models.Model):
    urun = models.ForeignKey(Urun)
    resim = FileBrowseField('Diger Modelin Resmi',max_length=200)
    aciklama = models.CharField("Diger Modelin Aciklamasi",max_length=100)

class YeniUrun(models.Model):
    urun = models.ForeignKey(Urun)
    def __unicode__(self):
        return self.urun.isim
    class Meta:
        verbose_name_plural = "Yeni Urunler"  
