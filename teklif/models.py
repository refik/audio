from django.db import models
from django.contrib.comments.models import Comment
from django.db.models.signals import post_init
from audio.bilgiGiris.models import Bilgi

#def teklif_yarat(sender,**kwargs):
#    print kwargs['instance'].yazi
#    print sender

#post_init.connect(teklif_yarat,sender=Bilgi)

class Durum(models.Model):
    isim = models.CharField('Durum', max_length=100)
    def __unicode__(self):
        return self.isim

class Teklif(models.Model):
    bilgi = models.OneToOneField(Bilgi)
    durum = models.ForeignKey(Durum,null=True,blank=True)
    def __unicode__(self):
        return self.bilgi.tip.isim

class TeklifYorum(Comment):
    durum = models.ForeignKey(Durum,null=True,blank=True)
