# coding: utf-8
from django.db import models
from datetime import datetime
from audio.bilgiGiris.mail import audiomail
from django.contrib.auth.models import User
from django.contrib.comments.moderation import CommentModerator, moderator

class Tip(models.Model):
    isim = models.CharField('Alan',max_length = 200)
    def __unicode__(self):
        return self.isim

class Sehir(models.Model):
    isim = models.CharField('Şehir',max_length = 200)
    def __unicode__(self):
        return self.isim

class Bilgi(models.Model):
    isim = models.CharField('İsim Soyisim', max_length = 50)
    sehir = models.ForeignKey(Sehir,null=True,blank=True)
    telefon = models.CharField('Telefon', max_length = 50,null=True,blank=True)
    email = models.EmailField('Email')
    firma = models.CharField('Firma', max_length = 200,null=True,blank=True)
    mesaj = models.TextField('Mesaj',null=True,blank=True)
    tip = models.ForeignKey(Tip)
    tarih = models.DateTimeField("Geliş Tarihi", auto_now_add=True)
    sorumlu = models.ManyToManyField(User,null=True,blank=True)
    class Meta: 
        verbose_name_plural = "Bilgiler"
    def __unicode__(self):
        return self.isim

class BilgiModerator(CommentModerator):
    email_notification = True
    def email(self, comment, content_object, request):
        audiomail("audioweb@audio.com.tr",[sorumlu.email for sorumlu in content_object.sorumlu.all()],str(content_object.tip) + u'\' na Yorum Yapıldı',u'%d nolu müşteri isteğine yapılan yorum\n%s\n31.222.163.32:8000/takip adresinden detaylı inceleyebilirsiniz'%(content_object.pk,comment))

moderator.register(Bilgi, BilgiModerator)
