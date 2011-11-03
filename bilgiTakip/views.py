from audio.bilgiGiris.models import Bilgi, Tip
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView
from django.utils.decorators import method_decorator

class TipListView(ListView):
    context_object_name = 'tipler'
    template_name = 'takip.html'

    def get_queryset(self):
        self.tipler = []
        for tip in self.request.user.profile.sorumluTip.all():
            if tip.isim == 'Teklif Formu':
                query = dict(self.request.GET.lists())
                for key in query.keys():
                    query[key] = query[key][0]
                bilgiler = tip.bilgi_set.all().filter(sorumlu__username__contains=self.request.user.username)
                bilgiler = bilgiler.filter(**query)
            else:
                bilgiler = tip.bilgi_set.all()
            self.tipler += [(tip.isim, bilgiler)]
        return self.tipler


class BilgiDetailView(DetailView):
    model = Bilgi
    template_name = 'istek.html'
    context_object_name = 'bilgi'

    def get_object(self):
        object = super(BilgiDetailView,self).get_object()
        if self.request.user in object.sorumlu.all():
            return object
        else:
            return None
