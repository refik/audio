from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi

class TeklifForm(ModelForm):
    TEMPLATE = 'bilgiGiris/teklif.html'
    KONU = 'Audio Teklif Formu'
    class Meta:
        model = Bilgi
        exclude = ('firma','sorumlu','tip')

class AkademiForm(ModelForm):
    TEMPLATE = 'bilgiGiris/teklif.html'
    class Meta:
        model = Bilgi
        exclude = ('mesaj','sorumlu')

class BultenForm(ModelForm):
    TEMPLATE = 'bilgiGiris/teklif.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','mesaj','sorumlu')

class IletisimForm(ModelForm):
    TEMPLATE = 'bilgiGiris/teklif.html'
    class Meta:
        model = Bilgi
        exclude = ('sehir','firma','sorumlu')





