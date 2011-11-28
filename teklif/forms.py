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
        print teklif.tutar, teklif.daire, teklif.durum, teklif.bilgi.pk
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
