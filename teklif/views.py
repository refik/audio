# coding: utf-8
from django.contrib.comments.views.comments import post_comment
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
from audio.ortakVeri.mail import audiomail
from audio.teklif.models import Durum
from audio.teklif.forms import TeklifYapildiForm

@require_POST
@csrf_exempt
def yapildi_yolla(request):
    form = TeklifYapildiForm(request.POST)
    if form.is_valid():
        yapilan = form.save()
        teklif = yapilan.teklif
        durum_mesaji = ''
        dosya_veri = request.FILES.get('dosya',None)
        if dosya_veri:
            dosya_icerik = ContentFile(dosya_veri.read())
            yapilan.dosya.save(dosya_veri.name, dosya_icerik)
            durum_mesaji += u"\n[Yoruma eklenen dosya: %s]" \
                            % yapilan.dosya.url
        if yapilan.durum is not None:
            yapilan.teklif.durum = yapilan.durum
            durum_mesaji += u"\n[Durum degistirildi: %s]" \
                            % yapilan.durum.isim
        if form.fields.has_key('tutar'):
            value = form.cleaned_data['tutar']
            if value:
                teklif.tutar = value
                durum_mesaji += u"\n[Tutar girildi: %d]" \
                                % value
        if form.fields.has_key('daire'):
            value = form.cleaned_data['daire']
            if value:
                teklif.daire = value
                durum_mesaji += u"\n[Daire sayisi girildi: %d]" \
                                % value
        if form.fields.has_key('rakip'):
            value = form.cleaned_data['rakip']
            if value:
                teklif.rakip = value
                durum_mesaji += u"\n[Kazanan rakip girildi: %s]" \
                                % value.isim
        if form.fields.has_key('delege'):
            value = form.cleaned_data['delege']
            if value:
                teklif.bilgi.sorumlu.add(value)
                durum_mesaji += u"\n[Is delege edildi: %s]" \
                                % value.get_full_name()
                audiomail('audioweb@audio.com.tr', [value.email], 'Audio Takip Sistemi', 'Size %s bir teklif delege etti, numarasi: %d.\n\nBu adresten bilgilere erisebilirsiniz: http://www.audio.com.tr/takip/%d' % (yapilan.kullanici.get_full_name(), teklif.bilgi.pk, teklif.bilgi.pk))
        if form.fields.has_key('sebep'):
            value = form.cleaned_data['sebep']
            if value:
                for v in value:
                    teklif.sebep.add(v)
                durum_mesaji += u"\n[Kaybetme sebepleri: %s]" \
                                % ', '.join([v.isim for v in list(value)])
        teklif.save()
        audiomail(
            "audioweb@audio.com.tr",
            [sorumlu.email for sorumlu in teklif.bilgi.sorumlu.all()] + \
            ['refik.rfk@gmail.com'],
            str(teklif.bilgi.tip) + u'\' na Yorum Yapıldı',
            u'%d nolu müşteri isteğine yapılan yorum\n\nMesaj: %s\n' \
            u'%s\n\nhttp://www.audio.com.tr/takip/%d adresinden ' \
            u'detaylı inceleyebilirsiniz' % (teklif.bilgi.pk, 
                                            yapilan.mesaj, 
                                            durum_mesaji,
                                            teklif.bilgi.pk))
        return redirect('/takip/%d' % yapilan.teklif.bilgi.pk)
    else:
        return render_to_response('onizleme.html', 
                                  {'form':form},
                                  context_instance=RequestContext(request))


