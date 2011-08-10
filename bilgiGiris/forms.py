from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi

class TeklifForm(ModelForm):
    TEMPLATE = 'bilgiGiris/teklif.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','sorumlu','tip')

class AkademiForm(ModelForm):
    TEMPLATE = 'bilgiGiris/varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('mesaj','sorumlu','tip')

class BultenForm(ModelForm):
    TEMPLATE = 'bilgiGiris/varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','mesaj','sorumlu','tip')

class IletisimForm(ModelForm):
    TEMPLATE = 'bilgiGiris/varsayilan.html'
    class Meta:
        model = Bilgi
        exclude = ('sehir','firma','sorumlu','tip')





