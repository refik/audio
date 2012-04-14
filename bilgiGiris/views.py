# coding: utf-8
from audio.bilgiGiris.forms import TeklifForm, BultenForm, AkademiForm, IletisimForm
from audio.bilgiGiris.models import Tip
from audio.teklif.models import OtomatikTeklif
from audio.ortakVeri.mail import audiomail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from django.db.models import Q
import json
SIRA = ['isim','email','sehir','firma','telefon','mesaj']

def mesajOlustur(sozluk):
    mesaj = ''
    for madde in SIRA:
        try:
            mesaj += madde.capitalize() + ': ' + unicode(sozluk[madde]) + '\n\n'
        except:
            pass
    return mesaj

def formSec(tip):
    if tip == 'teklif':
        return TeklifForm
    elif tip == 'bulten':
        return BultenForm
    elif tip == 'akademi':
        return  AkademiForm
    elif tip == 'iletisim':
        return IletisimForm
    else:
        raise Http404

def state_to_message(state, message):
    translations = {
        'single': 'apartman', 'multiple': 'site', 'villa': 'villa', 'two-doors': 'iki kapi', 'extra-monitor': 'ekstra sube', 
        'security': 'guvenlik', 'extra-camera': 'ekstra kamera', 'market': 'marketle konusma', 'doormen': 'kapici', 
        'light-base': 'isikli panel altligi', '': ''
    }
    t = lambda s: translations[s]
    info_tuple = (message, t(state['building']), state['apartment'], state['block'], 
        state['monitor']['id'], state['panel']['id'], 
        ', '.join([t(extra) for extra in state['extra']['monitors']] + [t(extra) for extra in state['extra']['panels']]), 
        state['price'])
    formatted_message = \
"""%s ****Otomatik teklif sisteminiden iletilmistir. Musterinin sistemden sectileri****
[Bina: %s | Toplam Daire: %i | Blok: %i] - 
[Monitor: %s | Panel: %s] - 
[Ekstra: %s] - 
[Fiyat: %iTL]""" % info_tuple
    return formatted_message

@csrf_exempt
def formIslem(request,tip):
    form = formSec(tip)
    record = None # Will be used if request is from auto offer
    sub_dict = lambda d, keys: {k:v for k,v in d.iteritems() if k in keys}
    if request.method == 'POST':
        post_dict = request.POST.copy() # Copy so it can be processed

        if post_dict.get('type','') == 'offer': # Check if it came from offer site
            message = post_dict.get('mesaj') # Original message
            state = post_dict.get('state') # State object to better inform
            print json.loads(state)
            request_info = state_to_message(json.loads(state), message) # Addition to original message
            post_dict.setlist('mesaj', [request_info]) # Update with new message
            sub_meta = sub_dict(request.META, ['REMOTE_ADDR', 'HTTP_USER_AGENT', 'HTTP_REFERER']) # Get customer info
            record = OtomatikTeklif(musteri=json.dumps(sub_meta), durum=state) # Pack usefull info

        bilgi = form(post_dict)
        if bilgi.is_valid():
            bilgi_db = bilgi.save()
            tip_db = Tip.objects.get(isim__contains = tip)
            bilgi_db.tip = tip_db 
            bilgi_db.save()

            # Save the record for auto offer
            if record: 
                record.teklif = bilgi_db.teklif
                record.save()

            sorumlular = User.objects.filter(profile__sorumluTip__isim__contains = tip)
            if tip == 'teklif':
                sorumlular = sorumlular.filter(profile__sorumluSehir__isim__contains = bilgi.cleaned_data['sehir']).exclude(Q(profile__birincil=True) | Q(profile__ikincil=True))
            gonderilecek = []
            for sorumlu in sorumlular:
                gonderilecek += [sorumlu.email]
                bilgi_db.sorumlu.add(sorumlu)
            konu = 'Audio ' + tip.capitalize() + ' Formu'
            mesaj = mesajOlustur(bilgi.cleaned_data)
            mesaj += u'http://www.audio.com.tr/takip/%d adresinden detayli inceleyebilirsiniz' % bilgi_db.pk
            audiomail('audioweb@audio.com.tr',gonderilecek + ['refik.rfk@gmail.com'],konu,mesaj)
            audiomail('audioweb@audio.com.tr', [bilgi.cleaned_data['email']],konu,'Isteginiz elimize ulasti, size en kisa zamanda cevap verecegiz.\n\nIstek kodunuz: #%d\n\nAudio Elektronik\nwww.audio.com.tr - 444 11 58\n\nnot: lutfen bu adrese cevap atmayin, kontrol edilmiyor.' % bilgi_db.id )
            yollaForm = form()
            geri_donus = 'İsteğiniz Elimize Ulaşmıştır'
        else:
            yollaForm = bilgi
            geri_donus = 'Lütfen Formdaki Hataları Kontrol Edin'
    else:
        yollaForm = form()
        geri_donus = ''
    return render_to_response(yollaForm.TEMPLATE,{'form':yollaForm, 'tip':tip,'mesaj':geri_donus},context_instance=RequestContext(request))

