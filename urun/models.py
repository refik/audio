# coding: utf-8
from django.db import models
from filebrowser.fields import FileBrowseField

SERI=(
     ("konsept","Konsept"),
     ("basic","Basic"),
     )

TIP =(
     ("goruntulu","Görüntülü"),
     ("sesli","Sesli"),
     )

class Sistem(models.Model):
    isim = models.CharField("Isim",max_length=200)
    tip = models.CharField("Tip", max_length = 50, choices =TIP)
    aciklama = models.TextField('Sistemin Aciklamasi')
    resim = FileBrowseField('Sistem Ikonu',max_length=150)
    sema = FileBrowseField('Sistemin Semasi',max_length=150,blank=True,null=True)
    class Meta: 
        verbose_name_plural = "Sistemler"
    def __unicode__(self):
        return unicode(self.isim)

class Ozellik(models.Model):
    isim = models.CharField("Aciklama", max_length = 200)
    class Meta:
        verbose_name_plural = "Ozellikler"
    def __unicode__(self):
        return unicode(self.isim)

class Kategori(models.Model):
    isim = models.CharField("Isim", max_length=50)
    slug = models.SlugField("Duzlestirilmis Isim", max_length = 50)
    class Meta:
        verbose_name_plural = "Kategoriler"
    def __unicode__(self):
        return unicode(self.isim)

class Urun(models.Model):
    isim = models.CharField("Isim", max_length=50)
    resim = FileBrowseField('Urunun Resmi', max_length=200) 
    sistem = models.ManyToManyField(Sistem,blank=True,null=True)
    kategori = models.ForeignKey(Kategori, related_name="UrunKategori", verbose_name="Kategori")
    seri = models.CharField("Seri",max_length=10,choices=SERI,blank=True,null=True)
    resim_yazi = models.CharField("Resim Alti Yazisi",max_length=200,blank=True,null=True)
    tanitim = models.TextField("Tanitim Metni",blank=True,null=True)
    ozellik = models.ManyToManyField(Ozellik, blank= True, null=True, related_name = "UrunOzellikler")
    slug = models.SlugField('Duzlestirilmis Isim')
    panel = models.ManyToManyField('self',blank=True,null=True)
    yeni = models.BooleanField('Yeni Urun, Anasayfada Gosterilsin',blank=True)
    class Meta:
        verbose_name_plural = "Urunler"
    def __unicode__(self):
        return self.isim

class DigerModel(models.Model):
    urun = models.ForeignKey(Urun)
    resim = FileBrowseField('Diger Modelin Resmi',max_length=200)
    aciklama = models.CharField("Diger Modelin Aciklamasi",max_length=100)
    class Meta:
        verbose_name_plural = 'Diger Modeller'
    def __unicode__(self):
        return unicode(self.aciklama)

