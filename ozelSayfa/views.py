from audio.ozelSayfa.models import Sayfa
from audio.haber.models import Haber
from django.shortcuts import render_to_response
from django.template import RequestContext

def medyaAl(sayfa_ismi):
    try:
        medya = Sayfa.objects.get(isim=sayfa_ismi).sayfamedya_set.all()
    except:
        return []
    return medya 

def anasayfa(request):
    medya = medyaAl('Anasayfa')
    try:
        haber = Haber.objects.filter(anasayfa=True)
    except:
        haber = []
    dataDict = dict([(m.isim, m)for m in medya] + [('haber',haber)])
    return render_to_response('ozelSayfa/anasayfa.html', dataDict, context_instance=RequestContext(request))    
