from audio.bilgiGiris.forms import TeklifForm, BultenForm, AkademiForm, IletisimForm
from audio.bilgiGiris.models import Tip
from audio.bilgiGiris.mail import audiomail
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from django.core.mail import send_mail
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

def formIslem(request,tip):
    form = formSec(tip)
    if request.method == 'POST':
        bilgi = form(request.POST)
        if bilgi.is_valid():
            bilgi_db = bilgi.save()
            tip_db = Tip.objects.get(isim__contains = tip)
            bilgi_db.tip = tip_db 
            bilgi_db.save()
            sorumlular = User.objects.filter(profile__sorumluTip__isim__contains = tip)
            if tip == 'teklif':
                sorumlular = sorumlular.filter(profile__sorumluSehir__isim__contains = bilgi.cleaned_data['sehir'])
            gonderilecek = []
            for sorumlu in sorumlular:
                gonderilecek += [sorumlu.email]
                bilgi_db.sorumlu.add(sorumlu)
            konu = 'Audio ' + tip + ' Formu'
            mesaj = mesajOlustur(bilgi.cleaned_data)
            audiomail('audioweb@audio.com.tr',['refik.rfk@gmail.com'],konu,mesaj)
            yollaForm = form()
            geri_donus = 'Isteginiz Elimize Ulasmistir'
        else:
            yollaForm = bilgi
            geri_donus = 'Lutfen Formdaki Hatalari Kontrol Edin'
    else:
        yollaForm = form()
        geri_donus = ''
    return render_to_response(yollaForm.TEMPLATE,{'form':yollaForm, 'tip':tip,'mesaj':geri_donus},context_instance=RequestContext(request))

