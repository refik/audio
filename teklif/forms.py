from django import forms
from django.contrib.comments.forms import CommentForm
from audio.teklif.models import TeklifYorum, Durum


class TeklifYorumFormu(CommentForm):
    durum = forms.ModelChoiceField(queryset=Durum.objects.all(),required=False)

    def get_comment_model(self):
        return TeklifYorum

    def get_comment_create_data(self):
        data = super(TeklifYorumFormu, self).get_comment_create_data()
        data['durum'] = self.cleaned_data['durum']
        return data
