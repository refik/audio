# coding: utf-8
from audio.bilgiGiris.forms import TeklifForm, BultenForm, AkademiForm, IletisimForm, StandForm, SunumKitForm
from audio.bilgiGiris.models import Tip
from audio.teklif.models import OtomatikTeklif
from audio.ortakVeri.mail import audiomail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.db.models import Q
from django.views.decorators.cache import never_cache
from audio.settings import GELISTIRME
from send_ax import AX_QUEUE_FOLDER, send_ax
import json
import os
SIRA = ['isim','email','sehir', 'ilce', 'adres', 'firma', 'no', 'telefon','mesaj']

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
    elif tip == 'stand':
        return StandForm
    elif tip == 'sunum-kiti':
        return SunumKitForm

    else:
        raise Http404

translations = {
    'single': 'apartman', 'multiple': 'site', 'villa': 'villa', 'two-doors': 'iki kapi', 'extra-monitor': 'ekstra sube', 
    'security': 'guvenlik', 'extra-camera': 'ekstra kamera', 'market': 'marketle konusma', 'doormen': 'kapici', 
    'light-base': 'isikli panel altligi', 'alarm': 'alarm karti', 'memory': 'fotograf hafiza karti', '': ''
}
t = lambda s: translations[s]
def state_to_message(state, message):
    info_tuple = (message, t(state['building']), state['apartment'], state['block'], 
        state['monitor']['id'], state['panel']['id'] if state.get('panel') else '-', 
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
    success = False
    form = formSec(tip)
    record = None # Will be used if request is from auto offer
    sub_dict = lambda d, keys: {k:v for k,v in d.iteritems() if k in keys}
    if request.method == 'POST':
        post_dict = request.POST.copy() # Copy so it can be processed

        offer_state = None
        message = post_dict.get('mesaj') # Original message
        if post_dict.get('type','') == 'offer': # Check if it came from offer site
            state = post_dict.get('state') # State object to better inform
            offer_state = json.loads(state)
            request_info = state_to_message(offer_state, message) # Addition to original message
            post_dict.setlist('mesaj', [request_info]) # Update with new message
            sub_meta = sub_dict(request.META, ['REMOTE_ADDR', 'HTTP_USER_AGENT', 'HTTP_REFERER']) # Get customer info
            record = OtomatikTeklif(musteri=json.dumps(sub_meta), durum=state) # Pack usefull info

        bilgi = form(post_dict)
        if bilgi.is_valid():
            bilgi_db = bilgi.save()
            if tip == 'teklif':
                path = os.path.join(AX_QUEUE_FOLDER, str(bilgi_db.pk))
                data = {'name': bilgi_db.isim, 
                        'city': bilgi_db.sehir.isim,
                        'county': bilgi_db.ilce.isim if bilgi_db.ilce else None,
                        'phone': bilgi_db.telefon,
                        'email': bilgi_db.email,
                        'message': message, #saving unaltered message
                        'buildingType': None,
                        'product': None}
                if offer_state:
                    data['buildingType'] = t[offer_state['building']]
                    data['quoteAmount'] = offer_state['price']
                    data['daireSayisi'] = offer_state['apartment']
                    data['blokSayisi'] = offer_state['block']
                    data['product'] = ("monitor: %s\n"
                                       "panel: %s\n"
                                       "ekstra: %s") % (offer_state['monitor']['id'], 
                                                        offer_state['panel']['id'] if offer_state.get('panel') else '',
                                                        ', '.join([t(extra) for extra in offer_state['extra']['monitors']] + [t(extra) for extra in offer_state['extra']['panels']])) 
                if not GELISTIRME:
                    with open(path, 'w+') as outfile:
                        json.dump(data, outfile)
                    send_ax()
            tip_db = Tip.objects.get(isim__contains = tip)
            bilgi_db.tip = tip_db 
            bilgi_db.save()
            sorumlular = User.objects.filter(profile__sorumluTip__isim__contains = tip)
            if tip == 'teklif':
                sorumlular = sorumlular.filter(profile__sorumluSehir__isim__contains = bilgi.cleaned_data['sehir'], profile__ucuncul=True)
            gonderilecek = []
            for sorumlu in sorumlular:
                gonderilecek += [sorumlu.email]
                bilgi_db.sorumlu.add(sorumlu)
            konu = 'Audio ' + tip.capitalize() + ' Formu'
            mesaj = mesajOlustur(bilgi.cleaned_data)
            mesaj += u'http://www.audio.com.tr/takip/%d adresinden detayli inceleyebilirsiniz' % bilgi_db.pk
            audiomail('audioweb@audio.com.tr',['refik.rfk@gmail.com'] + gonderilecek, konu, mesaj)
            audiomail('audioweb@audio.com.tr', [bilgi.cleaned_data['email']],konu,'İsteğiniz elimize ulaştı, size en kısa zamanda cevap vereceğiz.\n\nİstek kodunuz: #%d\n\nAudio Elektronik\nwww.audio.com.tr - 444 11 58\n\nnot: lütfen bu adrese cevap atmayın, kontrol edilmiyor.'.decode('utf-8') % bilgi_db.id )
            yollaForm = form()
            geri_donus = 'İsteğiniz Elimize Ulaşmıştır'
            success = True
        else:
            yollaForm = bilgi
            geri_donus = 'Lütfen Formdaki Hataları Kontrol Edin'
    else:
        yollaForm = form()
        geri_donus = ''
    
    # Save the record for auto offer, assume input is correct
    if record: 
        record.teklif = bilgi_db.teklif
        record.save()
        return HttpResponse('success')
    # Give user feedback if there is a mistake
    else:
        return render_to_response(yollaForm.TEMPLATE,{'form':yollaForm, 'tip':tip,'mesaj':geri_donus, 'basari': success},
                                  context_instance=RequestContext(request))

