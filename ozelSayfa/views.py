from audio.ozelSayfa.models import Sayfa
from audio.haber.models import Haber
from audio.urun.models import Urun
from django.shortcuts import render_to_response
from django.template import RequestContext

def medyaAl(sayfa_ismi):
    try:
        medya = Sayfa.objects.get(isim=sayfa_ismi).sayfalink_set.all()
    except:
        return []
    return medya 

def anasayfa(request):
    medya = medyaAl('Anasayfa')
    try:
        haber = Haber.objects.all()
        yeni_urun = Urun.objects.filter(yeni=True)
    except:
        haber = []
        yeni_urun = []
    dataDict = dict([(m.isim, m)for m in medya] + [('haber',haber)] + [('yeni_urun',yeni_urun)] )
    return render_to_response('anasayfa.html', dataDict, context_instance=RequestContext(request))    

def kaliteBelgelerimiz(request):
    medya = medyaAl('Kalite Belgelerimiz')
    return render_to_response('kalite_belgelerimiz.html', {'medya':medya}, context_instance=RequestContext(request)) 
