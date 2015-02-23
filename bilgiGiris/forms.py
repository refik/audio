from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi
from django.core.exceptions import ValidationError

class TeklifForm(ModelForm):
    TEMPLATE = 'teklif.html'

    def clean_telefon(self):
        telefon = self.cleaned_data['telefon']
        stripped = filter(lambda x: x.isdigit(), telefon)
        if stripped and stripped[0] == '0':
            stripped = stripped[1:]
        if len(stripped) != 10:
            raise ValidationError(u'Lutfen alan koduyla birlikte gecerli bir telefon numarasi giriniz.')
        return stripped

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
    TEMPLATE = 'dukkan_standi.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'ilce', 'firma', 'adres', 'no', 'telefon', 'email')

class SunumKitForm(ModelForm):
    TEMPLATE = 'sunum_kiti.html'
    class Meta:
        model = Bilgi
        fields = ('isim', 'sehir', 'ilce', 'firma', 'adres', 'no', 'telefon', 'email')
