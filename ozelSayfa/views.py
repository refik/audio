from audio.ozelSayfa.models import Sayfa
from audio.haber.models import Haber
from audio.urun.models import YeniUrun, Sistem
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
        yeni_urun = YeniUrun.objects.all()
    except:
        haber = []
        yeni_urun = []
    dataDict = dict([(m.isim, m)for m in medya] + [('haber',haber)] + [('yeni_urun',yeni_urun)] )
    return render_to_response('ozelSayfa/anasayfa.html', dataDict, context_instance=RequestContext(request))    

def sistem(request):
    goruntulu = Sistem.objects.filter(tip='goruntulu')
    sesli = Sistem.objects.filter(tip='sesli')
    return render_to_response('ozelSayfa/sistem.html',{'goruntulu':goruntulu,'sesli':sesli},context_instance=RequestContext(request)) 
