# coding: utf-8
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from audio.bilgiGiris.models import Bilgi
from audio.ortakVeri.mail import audiomail

class Sebep(models.Model):
    isim = models.CharField('Sebep', max_length=200)
    def __unicode__(self):
        return self.isim

class Rakip(models.Model):
    isim = models.CharField('Firma', max_length=200)
    def __unicode__(self):
        return self.isim

class Durum(models.Model):
    isim = models.CharField('Durum', max_length=100)
    kapali = models.BooleanField(default=False)
    def __unicode__(self):
        return self.isim

class Teklif(models.Model):
    bilgi = models.OneToOneField(Bilgi)
    durum = models.ForeignKey(Durum,null=True,blank=True)
    daire = models.IntegerField(null=True,blank=True)
    tutar = models.IntegerField(null=True,blank=True)
    dosya = models.FileField(upload_to='yukleme/teklif', null=True, blank=True)
    temsilci = models.ForeignKey(User, null=True, blank=True)
    son_eylem = models.DateTimeField(blank=True, null=True)
    class Meta:
        ordering = ['-bilgi__tarih']
    def __unicode__(self):
        return self.bilgi.tip.isim

class Yapildi(models.Model):
    kullanici = models.ForeignKey(User)
    teklif = models.ForeignKey(Teklif)
    mesaj = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    durum = models.ForeignKey(Durum, blank=True, null=True)
    dosya = models.FileField(upload_to='yukleme/teklif')
    rakip = models.ForeignKey(Rakip)
    sebep = models.ManyToManyField(Sebep)
    daire = models.IntegerField(null=True)
    tutar = models.IntegerField(null=True)
    delege = models.ForeignKey(User, related_name='delege_set')
    iscilik = models.IntegerField(null=True, blank=True)
    baglanti = models.TextField(blank=True)
    class Meta:
        ordering = ['-tarih']
 
class UserProxy(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return u'%s, %d' % (self.get_full_name(), Teklif.objects.filter(durum__kapali=False, bilgi__sorumlu=self).count())

@receiver(post_save,sender=Bilgi)
def teklif_yarat(sender,**kwargs):
    created_bilgi = kwargs['instance']
    try:
        created_bilgi.teklif
    except:
        if kwargs['created'] == False:
            if 'Teklif' in created_bilgi.tip.isim:
                t = Teklif(bilgi=kwargs['instance'])
                t.durum = Durum.objects.get(pk=1)
                kisi = User.objects.get(profile__ucuncul=True)
                t.temsilci = kisi
                t.son_eylem = created_bilgi.tarih
                t.save()

@receiver(post_save,sender=Yapildi)
def update_teklif(sender,**kwargs):
    yapildi = kwargs['instance']
    teklif = yapildi.teklif
    if yapildi.durum:
        teklif.durum = yapildi.durum
    if yapildi.dosya:
        teklif.dosya = yapildi.dosya
    if yapildi.daire:
        teklif.daire = yapildi.daire
    if yapildi.tutar:
        teklif.tutar = yapildi.tutar
    try:
        delege = User.objects.get(pk=yapildi.delege.pk)
        teklif.temsilci = delege
        teklif.bilgi.sorumlu.add(delege)
        audiomail('audioweb@audio.com.tr', [delege.email], 'Audio Takip Sistemi', 
                  'Size %s bir teklif delege etti, numarasi: %d.\n\nBu adresten bilgilere erisebilirsiniz: ' \
                  'http://www.audio.com.tr/teklif/%d' % 
                  (yapildi.kullanici.get_full_name(), teklif.pk, teklif.pk))
    except:
        pass

    teklif.son_eylem = yapildi.tarih
    teklif.save()
