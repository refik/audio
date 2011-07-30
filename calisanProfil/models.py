from django.db import models
from django.contrib.auth.models import User
from audio.bilgiGiris.models import Tip, Sehir

class CalisanGorev(models.Model):
    isim = models.CharField('Gorev Ismi',max_length=200)
    def __unicode__(self):
        return u'%s'%self.isim

class CalisanProfil(models.Model):
    user = models.OneToOneField(User,related_name='profile')
    sorumluSehir = models.ManyToManyField(Sehir)
    sorumluTip = models.ManyToManyField(Tip)
    gorev = models.ForeignKey(CalisanGorev,null=True)
    class Meta:
        verbose_name_plural = "Calisan Profilleri"
    def __unicode__(self):
        return u'%s'%self.user

