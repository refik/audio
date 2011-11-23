# coding: utf-8
from django import forms
from audio.teklif.models import TeklifYorum, Durum
from django.contrib.comments.forms import CommentForm
from django.contrib.auth.models import User

class TeklifYorumFormu(CommentForm):
    durum = forms.ModelChoiceField(queryset=Durum.objects.all(),required=False)
    dosya = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super(TeklifYorumFormu, self).__init__(*args, **kwargs)
        try:
            teklif = args[0].teklif
            if not teklif.tutar:
                self.fields['tutar'] = forms.IntegerField(required=False)
            if not teklif.daire:
                self.fields['daire'] = forms.IntegerField(required=False)
            if teklif.durum.isim == u'Eylem Yapılmadı' and u'İstanbul' in teklif.bilgi.sehir.isim:
                self.fields['delege'] = forms.ModelChoiceField(queryset=User.objects.filter(profile__sorumluTip__isim__contains='Teklif').exclude(profile__sorumluSehir__isim__contains=''), required=False)
        except:
            pass

    def get_comment_model(self):
        return TeklifYorum

    def get_comment_create_data(self):
        data = super(TeklifYorumFormu, self).get_comment_create_data()
        data['durum'] = self.cleaned_data['durum']
        data['dosya'] = self.cleaned_data['dosya']
        if self.cleaned_data.has_key('tutar'):
            data['tutar'] = self.cleaned_data['tutar']
        if self.cleaned_data.has_key('daire'):
            data['daire'] = self.cleaned_data['daire']
        if self.cleaned_data.has_key('delege'):
            data['delege'] = self.cleaned_data['delege']
        return data
