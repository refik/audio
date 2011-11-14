from audio.bilgiGiris.models import Bilgi, Tip
from audio.teklif.models import Durum, Teklif
from audio.calisanProfil.models import CalisanGorev
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import datetime, unicodedata, gviz_api

class TipListView(ListView):
    context_object_name = 'tipler'
    template_name = 'takip.html'

    def get_queryset(self):
        tip_ve_bilgi = []
        user = self.request.user
        if user.is_staff:
            tipler = Tip.objects.all()
        else:
            tipler = user.profile.sorumluTip.all()
        for tip in tipler:
            if tip.isim == 'Teklif Formu':
                query = dict(self.request.GET.lists())
                for key in query.keys():
                    try:
                        query[key] = int(query[key][0])
                    except:
                        query[key] = query[key][0]
                self.query = query
                if user.is_staff:
                    bilgiler = tip.bilgi_set.all()
                else:
                    bilgiler = tip.bilgi_set.all().filter(sorumlu=user)
                bilgiler = bilgiler.filter(**query)
            else:
                bilgiler = tip.bilgi_set.all()
            tip_ve_bilgi += [(tip.isim, bilgiler)]
        return tip_ve_bilgi

    def get_context_data(self,**kwargs):
        filtreler = []
        context = super(TipListView, self).get_context_data(**kwargs)
        gorevliler = User.objects.filter(profile__gorev__isim='Musteri Temsilcisi')
        durumlar = Durum.objects.all()
        bugun = datetime.date.today() 
        gun = datetime.timedelta(1)

        filtreler += [('sorumlu__pk',
                       'Temsilci',
                       [(gorevli.pk, gorevli.get_full_name()) for gorevli in gorevliler])]
        filtreler += [('teklif__durum__pk',
                       'Durum',
                       [(durum.pk, durum.isim) for durum in durumlar])]
        filtreler += [('teklif__durum__kapali',
                       'Kapali',
                       [(1,'Evet'),(0,'Hayir')])]
        filtreler += [('tarih__gt',
                       'Tarih',
                       [(str(bugun - i*i*gun),'%d gun icinde' % (i*i)) for i in range(1,6,1)])]

 
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


class IstatistikView(TemplateView):
    template_name = 'istatistik.html'

    def get_context_data(self,**kwargs):
        grafikler = []
        bugun = datetime.date.today()
        on_gun = datetime.timedelta(10)
        context = super(IstatistikView, self).get_context_data(**kwargs)
        durumlar = Durum.objects.all()
        teklifler = Teklif.objects.all()

        tanim = [("Durum", "string"),
                 ("Sayi", "number")]
        veri = [[durum.isim, durum.teklif_set.all().count()] for durum in durumlar]
        data_table = gviz_api.DataTable(tanim)
        data_table.LoadData(veri)
        json = data_table.ToJSon()
        grafikler += [(json, ' Su Anki Duruma Gore Teklif Sayisi', (800,400), 'PieChart')]

        tanim = [("Tarih", "string"),
                 ("Gelen Teklif Sayisi", "number")]
        veri = [[(bugun - on_gun*i).strftime('%d/%m/%Y'),teklifler.filter(bilgi__tarih__gt=bugun-on_gun*(i+1),
                                                                          bilgi__tarih__lt=bugun-on_gun*i).count()]                                                                          for i in range(4)]
        data_table = gviz_api.DataTable(tanim)
        data_table.LoadData(veri)
        json = data_table.ToJSon(order_by='Tarih')
        grafikler += [(json, 'Tarihe Gore Gelen Teklif', (800,400), 'ColumnChart')]

        context['grafikler'] = grafikler
        return context

class TemsilciDetailView(DetailView):
    model = User
    template_name = 'profil.html'
    context_object_name = 'calisan' 

    def get_object(self):
        object = super(TemsilciDetailView,self).get_object()
        gorev = CalisanGorev.objects.get(isim='Musteri Temsilcisi')
        if object.profile.gorev == gorev:
            return object
        else:
            return None

    def get_context_data(self,**kwargs):
        context =super(TemsilciDetailView, self).get_context_data(**kwargs)
        temsilci = self.get_object()
        teklifler = Teklif.objects.filter(bilgi__sorumlu=temsilci)
        context['kapali_is'] = teklifler.filter(durum__kapali=True).count()
        context['acik_is'] = teklifler.filter(durum__kapali=False).count()
        return context

class TemsilciListView(ListView):
    template_name = 'temsilciler.html'
    context_object_name = 'temsilciler'

    def get_queryset(self):
        temsilci_gorev= CalisanGorev.objects.get(isim='Musteri Temsilcisi')
        temsilciler = User.objects.filter(profile__gorev=temsilci_gorev) 
        return temsilciler.order_by('first_name')
