# coding: utf-8
from audio.bilgiGiris.models import Bilgi, Tip
from audio.teklif.models import Durum, Teklif, TeklifYorum
from audio.calisanProfil.models import CalisanGorev, Sehir
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import datetime
import unicodedata
import gviz_api

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
        gorevliler = User.objects.filter(
            profile__gorev__isim='Musteri Temsilcisi')
        sehirler = Sehir.objects.all()
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
        filtreler += [('sehir__pk',
                       'Sehir',
                       [(sehir.pk, sehir.isim) for sehir in sehirler])]

 
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
        on_gun = datetime.timedelta(5)
        context = super(IstatistikView, self).get_context_data(**kwargs)
        durumlar = Durum.objects.all()
        teklifler = Teklif.objects.all()
        alinan_isler = Durum.objects.get(isim__contains='Aldık').teklifyorum_set.all()
        kaybedilen_isler = Durum.objects.get(isim__contains='Kaybettik').teklifyorum_set.all()

        # Ilk Grafik
        tanim = [("Durum", "string"),
                 ("Sayi", "number")]
        veri = [[durum.isim, durum.teklif_set.all().count()] for durum in durumlar]
        data_table = gviz_api.DataTable(tanim)
        data_table.LoadData(veri)
        json = data_table.ToJSon()
        grafikler += [(json, ' Su Anki Duruma Gore Teklif Sayisi', 
                      (800,400), 'PieChart')]

        # Ikinci Grafik
        tanim = [("Tarih", "string"), ("Gelen Teklif Sayisi", "number")]
        veri = [
            [(bugun - on_gun*i).strftime('%d/%m/%Y'),
            teklifler.filter(bilgi__tarih__gt=bugun-on_gun*(i+1),
                             bilgi__tarih__lte=bugun-on_gun*i).count()] for i in range(4)]
        # veri = [['16/11', 22], ['12/11', 13], ['08/11', 2], ['04/11', 13], ['31/10', 14], ['27/10', 22], ['23/10', 15], ['19/10', 10], ['15/10', 9]]
        veri.reverse()
        data_table = gviz_api.DataTable(tanim)
        data_table.LoadData(veri)
        json = data_table.ToJSon()
        grafikler += [
            (json, 'Tarihe Gore Gelen Teklif', 
            (800,400), 'LineChart')]

        # Ucuncu Grafik
        tanim = [("Tarih", "string"), ("Aldigimiz Isler", "number"),
                 ("Kaybettigimiz Isler","number")]
        veri = [
            [(bugun - on_gun*i).strftime('%d/%m/%Y'),
            alinan_isler.filter(submit_date__gt=bugun-on_gun*(i+1),
                                submit_date__lte=bugun-on_gun*i).count(),
            kaybedilen_isler.filter(submit_date__gt=bugun-on_gun*(i+1),
                                    submit_date__lte=bugun-on_gun*i).count()] for i in range(4)]
        veri.reverse()
        data_table = gviz_api.DataTable(tanim)
        data_table.LoadData(veri)
        json = data_table.ToJSon()
        grafikler += [
            (json, 'Tarihe Gore Alip Kaybettigimiz Isler', 
            (800,400), 'ColumnChart')]
        print veri

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
        bilgiler = Bilgi.objects.filter(sorumlu=temsilci, tip__isim__contains='teklif')
        grafikler = []

        # Grafik
        tanim = [("Tarih", "string"), ("Saat", "number")]
        veri = [[yorumlar[0].content_object.tarih.strftime('%d/%m') ,round((float((yorumlar[0].submit_date - yorumlar[0].content_object.tarih).seconds) / 3600),2)] for yorumlar in [TeklifYorum.objects.filter(object_pk=bilgi.pk) for bilgi in [teklif.bilgi for teklif in teklifler]] if len(yorumlar) != 0]
        data_table = gviz_api.DataTable(tanim)
        data_table.LoadData(veri)
        json = data_table.ToJSon(order_by='Tarih')
        grafikler += [
            (json, 'Tarihe Gore Islerine Verdigi Reaksiyon Suresi', 
            (800,400), 'LineChart')]

        context['kapali_is'] = teklifler.filter(durum__kapali=True).count()
        context['acik_is'] = teklifler.filter(durum__kapali=False).count()
        context['grafikler'] = grafikler
        context['reaksiyon'] = datetime.timedelta(
            seconds=sum([tarih[1] for tarih in veri])/len(veri)*3600).__str__().split('.')[0]

        return context

class TemsilciListView(ListView):
    template_name = 'temsilciler.html'
    context_object_name = 'temsilciler'

    def get_queryset(self):
        temsilci_gorev= CalisanGorev.objects.get(isim='Musteri Temsilcisi')
        temsilciler = User.objects.filter(profile__gorev=temsilci_gorev) 
        return temsilciler.order_by('first_name')
