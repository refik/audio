from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi

class TeklifForm(ModelForm):
    TEMPLATE = 'teklif.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','sorumlu','tip')

class AkademiForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('mesaj','sorumlu','tip')

class BultenForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','mesaj','sorumlu','tip')

class IletisimForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('sehir','firma','sorumlu','tip')
