from audio.bilgiGiris.models import Bilgi, Tip
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def goster(request):
    tipler = Tip.objects.get(isim='Teklif Formu')
    return render_to_response('takip.html', {'tipler':[tipler]},context_instance=RequestContext(request))    
