from django.http import HttpResponse
from django.shortcuts import render_to_response
from audio.urun.models import Urun, Kategori
from audio.dokuman.models import Dokuman
from django.template import RequestContext

def urun(request,urun):
    istenenUrun = Urun.objects.get(slug=urun)
    dokuman = Dokuman.objects.filter(urun_sayfa=True)
    panelKonsept = istenenUrun.panel.filter(seri='konsept')
    panelBasic = istenenUrun.panel.filter(seri='basic')
    print panelKonsept
    return render_to_response('urun/urun.html',{'urun':istenenUrun, 'dokuman':dokuman, 'panelBasic':panelBasic,'panelKonsept':panelKonsept},context_instance=RequestContext(request))

def urunler(request,kategori):
    istenenKategori = Kategori.objects.get(slug=kategori).UrunKategori.all()
    konsept = istenenKategori.filter(seri='konsept')
    basic = istenenKategori.filter(seri='basic')
    ortak = istenenKategori.filter(seri='')
    return render_to_response('urun/kategori.html',{'konsept':konsept, 'basic':basic, 'ortak':ortak},context_instance=RequestContext(request))
