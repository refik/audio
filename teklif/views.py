# coding: utf-8
from django.contrib.comments.views.comments import post_comment
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from audio.ortakVeri.mail import audiomail
from audio.teklif.models import Durum, Teklif, Yapildi
from audio.teklif.forms import TeklifYapildiForm, TutarForm, DaireForm, DosyaForm, DelegeForm, SebepForm, MesajForm, DondurForm, AxaptaForm
import re

class OtomatikTeklif(TemplateView):
    template_name = 'auto_offer.html'

    def get_template_names(self):
        templates = super(OtomatikTeklif, self).get_template_names()
        agent_string = self.request.META['HTTP_USER_AGENT']
        if 'MSIE' in agent_string:
            agent_list = agent_string.split(' ')
            msie_version = float(re.sub(r'[a-zA-Z;]','',agent_list[agent_list.index('MSIE') + 1]))
            if msie_version < 8 and not 'Trident' in agent_string:
                templates.insert(0, 'upgrade_browser.html')
        return templates
    

class TeklifDosyaView(DetailView):
    template_name = 'iscilik.html'
    context_object_name = 'yapildi'
    model = Teklif

    def get_context_data(self, **kwargs):
        context = super(TeklifDosyaView, self).get_context_data(**kwargs)
        context['yapilanlar'] = self.get_object().yapildi_set.exclude(dosya='')
        return context

class NewView(DetailView):
    template_name = 'offer.html'
    context_object_name = 'offer'
    
    def get_object(self):
        user = self.request.user
        try:
            new_list = Teklif.objects.filter(pk__gt=self.kwargs['pk'])
            if not self.request.user.pk == 1:
                new_list = new_list.filter(bilgi__sorumlu=user)
            new_list.reverse()
            new = new_list[0]
        except:
            new = None
        return new

    def get_template_names(self):
        templates = super(NewView,self).get_template_names()
        if self.object == None:
            # This is an empty template
            templates.insert(0, 'success.html')
        return templates

#class IscilikTutarView(TemplateView):
#    template_name = 'iscilik_tutar.html'
#
#    def get_context_data(self, **kwargs):
#        context = super(IscilikTutarView, self).get_context_data(**kwargs)
#        iscilikli = Yapildi.objects.exclude(iscilik=None)
#        list_pk = self.request.GET.get('pks','')
#        if not list_pk:
#            return context
#        pk_numbers = [int(pk_string) for pk_string in list_pk.split('-')]
#        for pk_num in pk_numbers:
#            iscilikli = iscilikli.exclude(pk=pk_num)
#        iscilikler = [yapilan.iscilik for yapilan in iscilikli]
#        context['sayi'] = len(iscilikler)
#        context['toplam'] = sum(iscilikler)
#        return context

class DoneView(CreateView):
    template_name = 'done_form.html'
    success_url = '/teklif/success/'
    what_to_use = {'iletisim':[MesajForm, 3],
                   'iptal':[MesajForm, 8],
                   'sebep':[SebepForm, 7],
                   'delege':[DelegeForm, 2],
                   'dosya':[DosyaForm,5],
                   'aldik':[MesajForm,6],
                   'yonlendi':[MesajForm,4],
                   'tutar':[TutarForm],
                   'daire':[DaireForm],
                   'genel':[MesajForm,0],
                   'dondur':[DondurForm,9],
                   'axapta':[AxaptaForm]}

    def get_form_kwargs(self, *args, **kwargs):
        if self.request.method == 'GET':
            form_type = self.request.GET.get('form_type','')
            offer_pk = self.request.GET.get('pk','')
            user = self.request.user
            initial = {'kullanici': user.pk, 'teklif': offer_pk}
            try:
                initial.update({'durum': self.what_to_use[form_type][1]})
            except:
                pass
        else:
            initial = {}
        arguments = super(DoneView, self).get_form_kwargs(*args, **kwargs)
        arguments['initial'].update(initial)
        return arguments

    def get_form_class(self, *args, **kwargs):
        if self.request.method == 'GET':
            form_type = self.request.GET.get('form_type','')
        else:
            form_type = self.request.POST.get('form_type','')
        return self.what_to_use[form_type][0]


class OfferView(ListView):
    template_name = 'offers.html'
    context_object_name = 'offers'
    model = Teklif

    def get_queryset(self):
        user = self.request.user
        queryset = super(OfferView, self).get_queryset()

        # Needs a better distinction for top management
        if not(self.request.user.pk == 1 or self.request.user.pk == 54):
            queryset = queryset.filter(bilgi__sorumlu=user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(OfferView, self).get_context_data(**kwargs)
        self.get_queryset
        context['pk'] = self.kwargs.get('pk',0)
        return context


@require_POST
@csrf_exempt
def yapildi_yolla(request):
    form = TeklifYapildiForm(request.POST)
    if form.is_valid():
        yapilan = form.save()
        teklif = yapilan.teklif
        durum_mesaji = ''
        dosya_veri = request.FILES.get('dosya',None)
        if dosya_veri:
            dosya_icerik = ContentFile(dosya_veri.read())
            yapilan.dosya.save(dosya_veri.name, dosya_icerik)
            durum_mesaji += u"\n[Yoruma eklenen dosya: %s]" \
                            % yapilan.dosya.url
        if yapilan.durum is not None:
            yapilan.teklif.durum = yapilan.durum
            durum_mesaji += u"\n[Durum degistirildi: %s]" \
                            % yapilan.durum.isim
        if form.fields.has_key('tutar'):
            value = form.cleaned_data['tutar']
            if value:
                teklif.tutar = value
                durum_mesaji += u"\n[Tutar girildi: %d]" \
                                % value
        if form.fields.has_key('daire'):
            value = form.cleaned_data['daire']
            if value:
                teklif.daire = value
                durum_mesaji += u"\n[Daire sayisi girildi: %d]" \
                                % value
        if form.fields.has_key('rakip'):
            value = form.cleaned_data['rakip']
            if value:
                teklif.rakip = value
                durum_mesaji += u"\n[Kazanan rakip girildi: %s]" \
                                % value.isim
        if form.fields.has_key('delege'):
            value = form.cleaned_data['delege']
            if value:
                teklif.bilgi.sorumlu.add(value)
                durum_mesaji += u"\n[Is delege edildi: %s]" \
                                % value.get_full_name()
                audiomail('audioweb@audio.com.tr', [value.email], 'Audio Takip Sistemi', 'Size %s bir teklif delege etti, numarasi: %d.\n\nBu adresten bilgilere erisebilirsiniz: http://www.audio.com.tr/takip/%d' % (yapilan.kullanici.get_full_name(), teklif.bilgi.pk, teklif.bilgi.pk))
        if form.fields.has_key('sebep'):
            value = form.cleaned_data['sebep']
            if value:
                for v in value:
                    teklif.sebep.add(v)
                durum_mesaji += u"\n[Kaybetme sebepleri: %s]" \
                                % ', '.join([v.isim for v in list(value)])
        teklif.save()
        #audiomail(
        #    "audioweb@audio.com.tr",
        #    [sorumlu.email for sorumlu in teklif.bilgi.sorumlu.all()] + \
        #    ['refik.rfk@gmail.com'],
        #    str(teklif.bilgi.tip) + u'\' na Yorum Yapıldı',
        #    u'%d nolu müşteri isteğine yapılan yorum\n\nMesaj: %s\n' \
        #    u'%s\n\nhttp://www.audio.com.tr/takip/%d adresinden ' \
        #    u'detaylı inceleyebilirsiniz' % (teklif.bilgi.pk, 
        #                                    yapilan.mesaj, 
        #                                    durum_mesaji,
        #                                    teklif.bilgi.pk))
        return redirect('/takip/%d' % yapilan.teklif.bilgi.pk)
    else:
        return render_to_response('onizleme.html', 
                                  {'form':form},
                                  context_instance=RequestContext(request))


