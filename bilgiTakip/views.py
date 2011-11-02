from audio.bilgiGiris.models import Bilgi, Tip
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def goster(request):
    tipler = []
    for tip in request.user.profile.sorumluTip.all():
        if tip.isim == 'Teklif Formu':
            bilgiler = tip.bilgi_set.all().filter(sorumlu__username__contains=request.user.username)
        else:
            bilgiler = tip.bilgi_set.all()
        tipler += [(tip.isim, bilgiler)]
    return render_to_response('takip.html', {'tipler':tipler},context_instance=RequestContext(request))    
