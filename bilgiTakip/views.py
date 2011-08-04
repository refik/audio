from audio.bilgiGiris.models import Bilgi
from django.shortcuts import render_to_response
from django.template import RequestContext

def goster(request):
    bilgi = Bilgi.objects.all()
    return render_to_response('bilgiTakip/taban.html', {'bilgi':bilgi})    
