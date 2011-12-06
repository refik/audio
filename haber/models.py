from django.db import models
from filebrowser.fields import FileBrowseField
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from audio.settings import STATIC_ROOT, STATIC_URL
from audio.ortakVeri.sprite import PngSpriteCustom

class Haber(models.Model):
    baslik = models.CharField('Baslik',max_length=32)
    icerik = models.CharField('Icerik Yazisi', max_length=60)
    resim = FileBrowseField('Resim',max_length=200)
    class Meta:
        verbose_name_plural = "Haberler"
    def __unicode__(self):
        return unicode(self.baslik)

@receiver(post_save, sender=Haber)
def haber_sprite(sender, **kwargs):
    Haber.objects
    haber = kwargs['instance']
    haber.resim.version_generate('yeni_ufak')
    type = 'png-sprite'
    name = 'news'
    path = STATIC_ROOT + '/yukleme/'
    url = STATIC_URL + 'yukleme/'
    css_file = STATIC_ROOT + '/css/news.css'
    files = tuple([os.path.dirname(haber.resim.directory) + '/' + \
                   haber.resim.version_name('yeni_ufak') \
                   for haber in Haber.objects.all()])
    bundler = PngSpriteCustom(name, path, url, files, type, css_file)
    bundler.make_bundle(0)


