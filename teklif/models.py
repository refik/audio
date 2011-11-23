# coding: utf-8
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from audio.bilgiGiris.models import Bilgi

@receiver(post_save,sender=Bilgi)
def teklif_yarat(sender,**kwargs):
    try:
        kwargs['instance'].teklif
    except:
        if kwargs['created'] == False:
            if 'Teklif' in kwargs['instance'].tip.isim:
                t = Teklif(bilgi=kwargs['instance'])
                t.durum = Durum.objects.get(pk=1)
                t.kapali = False
                t.save()

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
    kaybedilen_rakip = models.ForeignKey(Rakip,blank=True,null=True)
    kaybetme_sebepleri = models.ManyToManyField(Sebep,blank=True,null=True)
    def __unicode__(self):
        return self.bilgi.tip.isim

class TeklifYorum(Comment):
    durum = models.ForeignKey(Durum,null=True,blank=True)
    dosya = models.FileField(upload_to='teklif',null=True,blank=True)
    daire = models.IntegerField(null=True,blank=True)
    tutar = models.IntegerField(null=True,blank=True)
    delege = models.ForeignKey(User,blank=True,null=True) 
