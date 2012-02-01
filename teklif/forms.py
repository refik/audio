# coding: utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.comments.forms import CommentForm
from django.contrib.auth.models import User
from audio.teklif.models import Teklif, Durum, Rakip, Sebep, Yapildi

class TeklifYapildiForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeklifYapildiForm, self).__init__(*args, **kwargs)
        if args:
            teklif_pk = int(args[0]['teklif'])
        else:
            teklif_pk = kwargs['initial']['teklif']    
        teklif = Teklif.objects.get(pk=teklif_pk)
        if not teklif.tutar:
            self.fields['tutar'] = forms.IntegerField(required=False)
        if not teklif.daire:
            self.fields['daire'] = forms.IntegerField(required=False)
        if teklif.durum.isim == u'İşi Kaybettik':
            if not teklif.rakip:
                self.fields['rakip'] = forms.ModelChoiceField(
                    queryset=Rakip.objects.all(),
                    required=False)
            if not teklif.sebep.all():
                self.fields['sebep'] = forms.ModelMultipleChoiceField(
                    queryset=Sebep.objects.all(), 
                    required=False)
        if teklif.durum.isim == u'Eylem Yapılmadı' and \
           u'İstanbul' in teklif.bilgi.sehir.isim:
            self.fields['delege'] = forms.ModelChoiceField(
                queryset=User.objects. \
                filter(profile__sorumluTip__isim__contains='Teklif') \
                .exclude(profile__sorumluSehir__isim__contains=''), 
                required=False)
    class Meta:
        model = Yapildi

class TutarForm(ModelForm):
    class Meta:
        model = Yapildi
        fields = ('tutar', 'kullanici', 'teklif')
        widgets = {
            'tutar': forms.TextInput(attrs={'class': 'span3'}),
        }

class DaireForm(ModelForm):
    class Meta:
        model = Yapildi
        fields = ('daire', 'kullanici', 'teklif')
        widgets = {
            'daire': forms.TextInput(attrs={'class': 'span3'}),
        }


class DosyaForm(ModelForm):
    class Meta:
        model = Yapildi
        fields = ('dosya', 'kullanici', 'teklif', 'durum')
        widgets = {
            'dosya': forms.FileInput(attrs={'class': 'span3'}),
        }


class DelegeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DelegeForm, self).__init__(*args, **kwargs)
        try:
            teklif_sehir = Teklif.objects.get(pk=kwargs['initial']['teklif']).bilgi.sehir
            new_queryset = self.fields['delege'].queryset.filter(profile__sorumluSehir=teklif_sehir, profile__birincil=True)
            self.fields['delege'].queryset = new_queryset
        except:
            # Form doesnt receive initial args
            # When it is initialized for validation
            # So I need this fucking try block
            pass
    class Meta:
        model = Yapildi
        fields = ('delege', 'kullanici', 'teklif', 'durum')
        widgets = {
            'delege': forms.Select(attrs={'class': 'span3'}),
        }


class SebepForm(ModelForm):
    class Meta:
        model = Yapildi
        fields = ('rakip', 'sebep', 'kullanici', 'teklif', 'durum')
        widgets = {
            'rakip': forms.Select(attrs={'class': 'span3'}),
            'sebep': forms.SelectMultiple(attrs={'class': 'span3'}),
        }


class MesajForm(ModelForm):
    class Meta:
        model = Yapildi
        fields = ('mesaj', 'kullanici', 'teklif', 'durum')
        widgets = {
            'mesaj': forms.Textarea(attrs={'class': 'span3', 'rows': '4'}),
        }


