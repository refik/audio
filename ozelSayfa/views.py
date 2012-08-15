from audio.ozelSayfa.models import Sayfa
from audio.haber.models import Haber
from audio.urun.models import Urun
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('http://www.audio.com.tr')

def medyaAl(sayfa_ismi):
    try:
        medya = Sayfa.objects.get(isim=sayfa_ismi).sayfalink_set.all()
    except:
        return []
    return medya 

def anasayfa(request):
    medya = medyaAl('Anasayfa')
    try:
        haber = Haber.objects.filter(anasayfa=True)
        yeni_urun = Urun.objects.filter(yeni=True)
    except:
        haber = []
        yeni_urun = []
    dataDict = dict([(m.isim, m)for m in medya] + [('haber',haber)] + [('yeni_urun',yeni_urun)] )
    return render_to_response('anasayfa.html', dataDict, context_instance=RequestContext(request))    

def stand_secimi(request):
    return render_to_response('stand_secimi.html', context_instance=RequestContext(request)) 

def numune_panosu(request):
    return render_to_response('numune_panosu.html', context_instance=RequestContext(request)) 

def baglanti_semalari(request):
    return render_to_response('baglanti_semalari.html', context_instance=RequestContext(request)) 


