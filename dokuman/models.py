from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from filebrowser.fields import FileBrowseField
from pyPdf import PdfFileReader
import subprocess
import os

class Dokuman(models.Model):
    isim = models.CharField('Isim',max_length=40)
    resim = FileBrowseField('Resim',max_length=200,blank=True,null=True,help_text='Urun sayfasinda gosterilmesini istiyorsaniz yukleyeceginiz dosyanin ilk sayfasinin resmini mutlaka ekleyin')
    dosya = FileBrowseField('Dosya', max_length=200, null=True)
    slug = models.SlugField('Duzlestirilmis Isim', help_text='Otomatik olarak yaratilir. Eger isimde sonradan bir degisiklik yaparsaniz bunu da ayni formatta degistirin.')
    urun_sayfa = models.BooleanField('Urun Sayfasinda Gosterilsin')
    class Meta:
        verbose_name_plural = "Dokumanlar"
    def __unicode__(self):
        return u"%s" % (self.isim)

@receiver(post_save, sender=Dokuman)
def dokuman_convert(sender, **kwargs):
    if kwargs['created'] is True:
        instance = kwargs['instance']
        dosya = instance.dosya
        klasor = dosya.filename_root + '-katalog-gorunumu-dosyalari'
        swfKlasor = os.path.dirname(dosya.path) + '/' + klasor
        default_storage.open(dosya.path).file.save_to_filename('/tmp/pdf')
        pdf = file('/tmp/pdf', 'rb')
        sayfa = PdfFileReader(pdf).getNumPages()
        pdf.close()
        for i in range(1, sayfa + 1):
            args = ['/usr/local/bin/pdf2swf',
                    '/tmp/pdf', '-o',
                    '/tmp/' + '%d.swf' % i,
                    '-f', '-T', '9', '-t', '-p',
                    '%d' % i, '-s', 'storeallcharacters']
            p = subprocess.Popen(args, stdout=subprocess.PIPE)
            for line in iter(p.stdout.readline, ''):
                if line[:5] == 'ERROR':
                    args += ['-s', 'poly2bitmap']
                    p = subprocess.Popen(args)
            p.wait()
            name = swfKlasor + '/' + '%d.swf' % i
            swf = open('/tmp/%d.swf' % i, 'rb').read()
            content = ContentFile(swf)
            default_storage.save(name, content)
