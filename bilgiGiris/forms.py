from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi

class TeklifForm(ModelForm):
    TEMPLATE = 'teklif.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'ilce', 'telefon', 'email', 'mesaj')

class AkademiForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'telefon', 'email', 'firma')

class BultenForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'telefon', 'email')

class IletisimForm(ModelForm):
    TEMPLATE = 'varsayilan.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'telefon', 'email', 'mesaj')

class StandForm(ModelForm):
    TEMPLATE = 'stand.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'ilce', 'firma', 'adres', 'no', 'telefon', 'email')
