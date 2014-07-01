# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from audio.bilgiGiris.models import Tip, Sehir, Bolge

class CalisanGorev(models.Model):
    isim = models.CharField('Gorev Ismi',max_length=200)
    class Meta:
        verbose_name_plural= "Calisan Gorevleri"
    def __unicode__(self):
        return unicode(self.isim)


class CalisanProfil(models.Model):
    user = models.OneToOneField(User,related_name='profile',help_text='Bu profilin bagli oldugu kullanici')
    sorumluSehir = models.ManyToManyField(Sehir,help_text='Bu kullanicinin sorumlu oldugu sehirler',null=True,blank=True)
    sorumluBolge = models.ManyToManyField(Bolge,help_text='Bu kullanicinin sorumlu oldugu bolgeler',null=True,blank=True)
    sorumluTip = models.ManyToManyField(Tip,help_text='Bu kullanicinin sorumlu oldugu form tipleri',null=True,blank=True)
    telefon = models.CharField('Telefon Numarasi',max_length=200,help_text='(xxxx) xxx xx xx formunda girin')
    gorev = models.ForeignKey(CalisanGorev)
    birincil = models.BooleanField()
    ikincil = models.BooleanField()
    ucuncul = models.BooleanField()
    class Meta:
        verbose_name_plural = "Calisan Profilleri"
    def __unicode__(self):
        return unicode(self.user)
    def tam_isim(self):
        return self.user.get_full_name()

