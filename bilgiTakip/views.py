from audio.bilgiGiris.models import Bilgi, Tip
from audio.teklif.models import Durum
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import datetime

class TipListView(ListView):
    context_object_name = 'tipler'
    template_name = 'takip.html'

    def get_queryset(self):
        self.tipler = []
        for tip in self.request.user.profile.sorumluTip.all():
            if tip.isim == 'Teklif Formu':
                query = dict(self.request.GET.lists())
                for key in query.keys():
                    try:
                        query[key] = int(query[key][0])
                    except:
                        query[key] = query[key][0]
                self.query = query
                bilgiler = tip.bilgi_set.all().filter(sorumlu__username=self.request.user.username)
                bilgiler = bilgiler.filter(**query)
            else:
                bilgiler = tip.bilgi_set.all()
            self.tipler += [(tip.isim, bilgiler)]
        return self.tipler

    def get_context_data(self,**kwargs):
        filtreler = []
        context = super(TipListView, self).get_context_data(**kwargs)
        gorevliler = User.objects.filter(profile__gorev__isim='Musteri Temsilcisi')
        durumlar = Durum.objects.all()
        bugun = datetime.date.today() 
        gun = datetime.timedelta(1)

        filtreler += [('sorumlu__pk',
                       'Temsilci',
                       [(gorevli.pk, gorevli.first_name + ' ' + gorevli.last_name) for gorevli in gorevliler])]
        filtreler += [('teklif__durum__pk',
                       'Durum',
                       [(durum.pk, durum.isim) for durum in durumlar])]
        filtreler += [('teklif__durum__kapali',
                       'Kapali',
                       [(1,'Evet'),('0','Hayir')])]
        filtreler += [('tarih__gt',
                       'Tarih',
                       [('%s' % (bugun),'Bugun Icinde'),            ('%s' % (bugun - 3*gun),'Uc Gun Icinde'),
                        ('%s' % (bugun - 7*gun),'Bu Hafta Icinde'), ('%s' % (bugun - 30*gun),'Bu Ay Icinde')])]

        context['filtreler'] = [ { 'sorgu' : filtre[0],
                                   'isim' : filtre[1],
                                   'maddeler' : filtre[2],
                                   'secili' : self.query.get(filtre[0], None) } for filtre in filtreler ]
        return context


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
