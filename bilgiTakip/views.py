from audio.bilgiGiris.models import Bilgi, Tip
from django.shortcuts import render_to_response
from django.template import RequestContext

def goster(request):
    tipler = Tip.objects.all()
    return render_to_response('takip.html', {'tipler':tipler},context_instance=RequestContext(request))    
