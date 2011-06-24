from audio.bilgiGiris.forms import TeklifForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404

def formSec(tip):
    if tip == 'teklif':
        return TeklifForm
    elif tip == 'bulten':
        return BultenForm
    elif tip == 'akademi':
        return  AkademiForm
    elif tip == 'iletisim':
        return IletisimForm
    else:
        raise Http404

def formIslem(request,tip):
    form = formSec(tip)
    if request.method == 'POST':
        bilgi = form(request.POST)
        bilgi.save()
    return render_to_response(form().TEMPLATE,{'form':form()},context_instance=RequestContext(request))

