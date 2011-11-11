# coding: utf-8
from django.db import models
from django.db.models.signals import pre_save, post_save
from audio.bilgiGiris.models import Bilgi
from django.contrib.comments.models import Comment
from audio.bilgiGiris.mail import audiomail

def yorum_yonet(sender,**kwargs):
    durum_mesaji = u''
    yorum = kwargs['instance']
    try:
        teklif = yorum.content_object.teklif
        if yorum.durum != None: 
            teklif.durum = yorum.durum
            durum_mesaji = u"(Bu işin durumu '%s' olarak değiştirildi)" % teklif.durum.isim
            yorum.comment += ' %s' % durum_mesaji
            yorum.content_object.teklif.save()
    except:
        pass
    #audiomail("audioweb@audio.com.tr",[sorumlu.email for sorumlu in yorum.content_object.sorumlu.all()] + ['refik.rfk@gmail.com'],str(yorum.content_object.tip) + u'\' na Yorum Yapıldı',u'%d nolu müşteri isteğine yapılan yorum\n\n%s %s\n\nhttp://www.audio.com.tr/takip/%d adresinden detaylı inceleyebilirsiniz'%(yorum.content_object.pk,yorum.comment,durum_mesaji,yorum.content_object.pk))

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

post_save.connect(teklif_yarat,sender=Bilgi)
pre_save.connect(yorum_yonet,sender=TeklifYorum)


