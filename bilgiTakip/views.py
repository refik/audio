from audio.bilgiGiris.models import Bilgi, Tip
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator

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

class TakipDetailView(DetailView):
    model = Bilgi
    template_name = 'istek.html'
    context_object_name = 'bilgi'

    def get_object(self):
        object = super(TakipDetailView,self).get_object()
        if self.request.user in object.sorumlu.all():
            return object
        else:
            return None
    
    @method_decorator(login_required) 
    def dispatch(self,*args,**kwargs):
        return super(TakipDetailView,self).dispatch(*args,**kwargs) 
