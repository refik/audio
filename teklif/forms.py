from django import forms
from audio.teklif.models import TeklifYorum, Durum
from django.contrib.comments.forms import CommentForm

class TeklifYorumFormu(CommentForm):
    durum = forms.ModelChoiceField(queryset=Durum.objects.all(),required=False)
    dosya = forms.FileField(required=False)

    def get_comment_model(self):
        return TeklifYorum

    def get_comment_create_data(self):
        data = super(TeklifYorumFormu, self).get_comment_create_data()
        data['durum'] = self.cleaned_data['durum']
        return data
