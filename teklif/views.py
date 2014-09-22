# coding: utf-8
from django.contrib.comments.views.comments import post_comment
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.db.models import Q
from audio.ortakVeri.mail import audiomail
from audio.teklif.models import Durum, Teklif, Yapildi
from audio.teklif.forms import TeklifYapildiForm, TutarForm, DaireForm, DosyaForm, DelegeForm, SebepForm, MesajForm, DondurForm, AxaptaForm
from audio.bilgiGiris.models import Bolge, Sehir, Tip
from audio.calisanProfil.models import CalisanProfil, CalisanGorev
from django.views.decorators.cache import never_cache
import random
import string
import re

def generate_password():
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10)) 

class OtomatikTeklif(TemplateView):
    template_name = 'auto_offer.html'

    def get_template_names(self):
        templates = super(OtomatikTeklif, self).get_template_names()
        agent_string = self.request.META['HTTP_USER_AGENT']
        if 'MSIE' in agent_string:
            agent_list = agent_string.split(' ')
            msie_version = float(re.sub(r'[a-zA-Z;]','',agent_list[agent_list.index('MSIE') + 1]))
            if msie_version < 8 and not 'Trident' in agent_string and False:
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


class IscilikTutarView(TemplateView):
    template_name = 'confirm.html'


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
            offer_pk = self.request.GET.get('pk','')
            form_class = self.what_to_use[form_type][0]
            form_class.base_fields['teklif'].queryset = Teklif.objects.filter(pk=offer_pk)
        else:
            form_type = self.request.POST.get('form_type','')
            form_class = self.what_to_use[form_type][0]
            offer_pk = self.request.POST.get('teklif','')
            form_class.base_fields['teklif'].queryset = Teklif.objects.filter(pk=int(offer_pk))
      
        return form_class

class YonetimView(ListView):
    template_name = 'yonetim.html'
    context_object_name = 'bolgeler'
    model = Bolge

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['sehirler'] = Sehir.objects.all()
        context['temsilciler'] = User.objects.filter(Q(profile__birincil=True) | Q(profile__ikincil=True), is_active=True).order_by('first_name')
        return context

@csrf_exempt
def sifremi_unuttum(request):
    mail = request.POST['email']
    user = User.objects.filter(email=mail, is_active=True)
    if user:
        user = user[0]
        password = generate_password()
        user.set_password(password)
        audiomail('audioweb@audio.com.tr', [user.email], 'Audio Kullanici Sifre', """
Merhaba %s,

Bu maili, Audio Teklif sitesi girisindeki "sifremi unuttum" butonuna tikladiginiz icin aliyorsunuz. Bir yanlislik oldugunu dusunuyorsaniz lutfen birim yoneticinizle irtibata gecin.

Kullanici adiniz: %s
Yeni gecici sifreniz: %s

Lutfen bu sifreyi http://www.audio.com.tr/sifre-degistir adresinden degistirin.""" % (user.get_full_name(), user.username, password))
        print 'sifre', password
        user.save()
    return HttpResponse('Lutfen maillarinizi kontrol edin')


@csrf_exempt
def yonetim_degistir(request):
    data = request.POST
    print data
    if data['action'] == 'bolge-sehir-ekle':
        sehir = Sehir.objects.get(pk=data['sehir_pk'])
        sehir.bolge_id = data['bolge_pk']
        sehir.save()
        print sehir, 'changed bolge', sehir.bolge_id
    elif data['action'] == 'temsilci-bolgeden-cikart':
        user = User.objects.get(pk=data['user_pk'])
        bolge = Bolge.objects.get(pk=data['bolge_pk'])
        user.profile.sorumluBolge.remove(bolge)
        print user, 'removed bolge', bolge
    elif data['action'] == 'bolge-temsilci-ekle':
        user = User.objects.get(pk=data['user_pk'])
        bolge = Bolge.objects.get(pk=data['bolge_pk'])
        user.profile.sorumluBolge.add(bolge)
        print user, 'added bolge', bolge
    elif data['action'] =='temsilci-sifre-sifirla':
        user = User.objects.get(pk=data['user_pk'])
        print user, 'sent password deletion' 
    elif data['action'] =='temsilci-sil':
        user = User.objects.get(pk=data['user_pk'])
        user.is_active = False
        user.save()
        print user, 'deactivated' 
    elif data['action'] =='temsilci-yarat':
        bolge = Bolge.objects.get(isim=data['bolge'])
        user = User(first_name=data['isim'], last_name=data['isim'], username=data['kullanici-adi'])
        password = generate_password()
        user.set_password(password)
        user.save()
        gorev = CalisanGorev.objects.get(isim='Musteri Temsilcisi')
        profil = CalisanProfil(user=user, birincil=True, gorev=gorev)
        profil.save()
        tip = Tip.objects.get(isim='Teklif Formu')
        profil.sorumluTip.add(tip)
        user.profile.sorumluBolge.add(bolge)
        audiomail('audioweb@audio.com.tr', [user.email], 'Audio Teklif Kullanici', """
Merhaba %s,

Web teklifleri sitesi icin bilgileriniz su sekilde:
kullanici adi: %s
sifre : %s

Sayfanin adresi http://www.audio.com.tr/teklif
Lutfen sifrenizi su adresten degistirin http://www.audio.com.tr/sifre-degistir

Iyi calismalar""" % (user.get_full_name(), user.username, password))

    return redirect('/teklif/yonetim/')


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

        hepsi = self.request.GET.get('hepsi')
        if hepsi != 'evet':
            queryset = queryset.filter(Q(durum__kapali=False) | Q(durum__isim='Donduruldu'))

        return queryset

    def get_context_data(self, **kwargs):
        context = super(OfferView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk',0)
        context['sorumlular'] = User.objects.filter(Q(profile__birincil=True) | Q(profile__ikincil=True)).order_by('first_name')
        return context


@require_POST
@csrf_exempt
@never_cache
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


