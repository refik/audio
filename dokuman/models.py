from django.db import models
from filebrowser.fields import FileBrowseField

class Dokuman(models.Model):
    isim = models.CharField('Isim',max_length=40)
    resim = FileBrowseField('Resim',max_length=200,blank=True,null=True,help_text='Urun sayfasinda gosterilmesini istiyorsaniz yukleyeceginiz dosyanin ilk sayfasinin resmini mutlaka ekleyin')
    dosya = FileBrowseField('Dosya',max_length=200,null=True,help_text='Eger varolan bir dokumanin dosyasin ayni isimli bir dosyayla degistiriyorsaniz, medya yoneticisinden otomatik olarak yaratilan dosya-ismi-katalog-gorunumu-dosyalari klasorunu mutlaka silin. Yeni ekleyeceginiz dosya icin bu klasor otomatik olarak yeniden yaratilacaktir.')
    slug = models.SlugField('Duzlestirilmis Isim',help_text='Otomatik olarak yaratilir. Eger isimde sonradan bir degisiklik yaparsaniz bunu da ayni formatta degistirin.')
    urun_sayfa = models.BooleanField('Urun Sayfasinda Gosterilsin')
    class Meta:
        verbose_name_plural = "Dokumanlar"
    def __unicode__(self):
        return u"%s" % (self.isim)

