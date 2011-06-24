from audio.bilgiGiris.forms import TeklifForm, BultenForm, AkademiForm, IletisimForm
from django.contrib.auth.models import User
from audio.calisanProfil.models import CalisanProfil
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
SIRA = ['isim','email','sehir','firma','telefon','mesaj']

def mesajOlustur(sozluk):
    mesaj = ''
    for madde in SIRA:
        try:
            mesaj += madde + ': ' + sozluk[madde] + '\n'
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

def sorumluBul(tip,sehir):
    sorumlular = User.objects.filter(profile__sorumluTip__isim__contains = tip)
    if sehir != None:
        sorumlular = sorumlular.filter(profile__sorumluSehir__isim__contains = sehir)
    return sorumlular

def formIslem(request,tip):
    form = formSec(tip)
    if request.method == 'POST':
        bilgi = form(request.POST)
        if bilgi.is_valid():
            bilgi.save()
            if bilgi.cleaned_data['tip'].isim == 'teklif':
                sehir = bilgi.cleaned_data['sehir']
            else:
                sehir = None
            sorumlular = sorumluBul(tip,sehir)
            gonderilecek = []
            for sorumlu in sorumlular:
                gonderilecek += [sorumlu.email]
            konu = bilgi.KONU
            mesaj = mesajOlustur(bilgi.cleaned_data)
            #test icin
            print [gonderilecek, konu, mesaj]
            #test bitti
    return render_to_response(form().TEMPLATE,{'form':form()},context_instance=RequestContext(request))

