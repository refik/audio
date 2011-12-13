# coding: utf-8
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from filebrowser.fields import FileBrowseField
from audio.settings import STATIC_ROOT

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

@receiver(post_save, sender=Urun)
def yeniurun_sprite(sender, **kwargs):
    pic_urun = [urun.resim for urun in Urun.objects.filter(yeni=True)]
    pic_ver = [pic.version_generate('yeni_ufak') for pic in pic_urun]
    pictures = [pic.name for pic in pic_ver]
    for picture in pictures:
        save_to_local(picture, '/tmp/%s' % os.path.basename(picture))
    type = 'png-sprite'
    name = 'products'
    path = '/tmp/'
    url = STATUC_URL + 'resim/sprite/'
    css_file = STATIC_ROOT + '/css/products.css'
    files = tuple([os.path.basename(picture) for picture in pictures])
    bundler = PngSpriteCustom(name, path, url, files, type, css_file)
    bundler.make_bundle(0)

class DigerModel(models.Model):
    urun = models.ForeignKey(Urun)
    resim = FileBrowseField('Diger Modelin Resmi',max_length=200)
    aciklama = models.CharField("Diger Modelin Aciklamasi",max_length=100)
    class Meta:
        verbose_name_plural = 'Diger Modeller'
    def __unicode__(self):
        return unicode(self.aciklama)

