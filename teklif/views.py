# coding: utf-8
from django.contrib.comments.views.comments import post_comment
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.dispatch import receiver
from audio.bilgiGiris.mail import audiomail
from audio.teklif.models import TeklifYorum
from audio.settings import MEDIA_ROOT

DOSYA = None

# Bu fonksiyon burda kalmazsa dosya save etme calismaz
@receiver(pre_save,sender=TeklifYorum)
def yorum_yonet(sender,**kwargs):
    durum_mesaji = u''
    yorum = kwargs['instance']
    if DOSYA:
        yorum.dosya.save(DOSYA['isim'], DOSYA['icerik'],save=False)
    try:
        teklif = yorum.content_object.teklif
        if yorum.durum != None:
            eski_durum = teklif.durum
            yeni_durum = yorum.durum
            teklif.durum = yeni_durum
            durum_mesaji = u"\n[İşin durumu: %s -> %s ]" % (eski_durum.isim, yeni_durum.isim)
            if yorum.dosya:
                durum_mesaji += u"\n Yoruma eklenen dosya: %s" % yorum.dosya.url
            yorum.content_object.teklif.save()
    except:
        pass
    audiomail("audioweb@audio.com.tr",[sorumlu.email for sorumlu in yorum.content_object.sorumlu.all()] + ['refik.rfk@gmail.com'],str(yorum.content_object.tip) + u'\' na Yorum Yapıldı',u'%d nolu müşteri isteğine yapılan yorum\n\n%s %s\n\nhttp://www.audio.com.tr/takip/%d adresinden detaylı inceleyebilirsiniz'%(yorum.content_object.pk,yorum.comment,durum_mesaji,yorum.content_object.pk))

def yorum_dosya(request):
    global DOSYA
    dosya_veri = request.FILES.get('dosya',None)
    if dosya_veri:
        dosya_icerik = ContentFile(dosya_veri.read())
        DOSYA = {'isim': dosya_veri.name, 'icerik': dosya_icerik}
    else:
        DOSYA = None
    return post_comment(request)

