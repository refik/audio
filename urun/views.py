from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from audio.urun.models import Urun, Kategori, Sistem
from audio.dokuman.models import Dokuman
from django.template import RequestContext

def sistem(request):
    goruntulu = Sistem.objects.filter(tip='goruntulu')
    sesli = Sistem.objects.filter(tip='sesli')
    return render_to_response('sistem.html',{'goruntulu':goruntulu,'sesli':sesli},context_instance=RequestContext(request)) 

def urun(request,urun):
    istenenUrun = get_object_or_404(Urun, slug=urun)
    dokuman = Dokuman.objects.filter(urun_sayfa=True)
    if not 'panel' in istenenUrun.kategori.isim:
        panelKonsept = istenenUrun.panel.filter(seri='konsept')
        panelBasic = istenenUrun.panel.filter(seri='basic')
        if not panelBasic and not panelKonsept:
            panelJenerik = istenenUrun.panel.all()
        else:
            panelJenerik = []
        print panelBasic, panelKonsept, panelJenerik
    else:
        panelKonsept, panelBasic = [], []
    return render_to_response('urun.html',{'urun':istenenUrun, 'dokuman':dokuman, 'panelBasic':panelBasic,'panelJenerik':panelJenerik,'panelKonsept':panelKonsept},context_instance=RequestContext(request))

def urunler(request,kategori):
    kategori_db = get_object_or_404(Kategori, slug=kategori)
    istenenKategori = kategori_db.UrunKategori.all()
    konsept = istenenKategori.filter(seri='konsept')
    basic = istenenKategori.filter(seri='basic')
    ortak = istenenKategori.filter(seri=None)
    return render_to_response('kategori.html',{'baslik': kategori_db.isim,'konsept':konsept, 'basic':basic, 'ortak':ortak},context_instance=RequestContext(request))
