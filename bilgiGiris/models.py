# coding: utf-8
from django.db import models
from datetime import datetime
from audio.ortakVeri.mail import audiomail
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

class Ilce(models.Model):
    sehir = models.ForeignKey(Sehir)
    isim = models.CharField('İlçe', max_length = 200)
    def __unicode__(self):
        return self.isim

class Bilgi(models.Model):
    isim = models.CharField('İsim Soyisim', max_length = 50)
    sehir = models.ForeignKey(Sehir)
    ilce = models.ForeignKey(Ilce)
    telefon = models.CharField('Telefon', max_length = 50)
    email = models.EmailField('Email')
    firma = models.CharField('Firma', max_length = 200)
    mesaj = models.TextField('Mesaj')
    tip = models.ForeignKey(Tip)
    tarih = models.DateTimeField("Geliş Tarihi", auto_now_add=True)
    sorumlu = models.ManyToManyField(User,null=True,blank=True)
    class Meta: 
        verbose_name_plural = "Bilgiler"
        ordering = ['-tarih']

    def __unicode__(self):
        return self.isim
