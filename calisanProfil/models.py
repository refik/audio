from django.db import models
from django.contrib.auth.models import User
from audio.bilgiGiris.models import Tip, Sehir

class CalisanProfil(models.Model):
    user = models.OneToOneField(User)
    sorumluSehir = models.ManyToManyField(Sehir)
    sorumluTip = models.ManyToManyField(Tip)
    class Meta:
        verbose_name_plural = "Calisan Profilleri"
    def __unicode__(self):
        return self.user
