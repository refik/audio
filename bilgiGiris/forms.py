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
        exclude = ('mesaj','sorumlu','tip','ilce')

class BultenForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','mesaj','sorumlu','tip','ilce')

class IletisimForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('sehir','ilce','firma','sorumlu','tip')
