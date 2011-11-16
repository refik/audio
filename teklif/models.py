# coding: utf-8
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.comments.models import Comment
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

class Durum(models.Model):
    isim = models.CharField('Durum', max_length=100)
    kapali = models.BooleanField(default=False)
    def __unicode__(self):
        return self.isim

class Teklif(models.Model):
    bilgi = models.OneToOneField(Bilgi)
    durum = models.ForeignKey(Durum,null=True,blank=True)
    def __unicode__(self):
        return self.bilgi.tip.isim

class TeklifYorum(Comment):
    durum = models.ForeignKey(Durum,null=True,blank=True)
    dosya = models.FileField(upload_to='teklif',null=True,blank=True)

