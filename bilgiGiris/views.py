from audio.bilgiGiris.forms import TeklifForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404

def formGoster(request,tip):
    if tip == 'teklif':
        template = 'bilgiGiris/teklif.html'
    elif tip == 'bulten' or tip == 'akademi' or tip == 'iletisim':
        template = 'bilgiGiris/akademi.bulten.iletisim.html'
    else:
        raise Http404
    form = TeklifForm()
    return render_to_response(template,{'form':form},context_instance=RequestContext(request))
    
