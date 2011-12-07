from django.db import models
from filebrowser.fields import FileBrowseField
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from audio.settings import STATIC_ROOT, STATIC_URL
from audio.ortakVeri.sprite import PngSpriteCustom
from audio.ortakVeri.file import save_to_local

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
    pic_haber = [haber.resim for haber in Haber.objects.all()]
    pic_ver = [pic.version_generate('haber_ufak') for pic in pic_haber]
    pictures = [pic.name for pic in pic_ver]
    for picture in pictures:
        save_to_local(picture,'/tmp/%s' % os.path.basename(picture))
    type = 'png-sprite'
    name = 'news'
    path = '/tmp/'
    url = STATIC_URL + 'resim/sprite/'
    css_file = STATIC_ROOT + '/css/news.css'
    files = tuple([os.path.basename(picture) for picture in pictures])
    bundler = PngSpriteCustom(name, path, url, files, type, css_file)
    bundler.make_bundle(0)

