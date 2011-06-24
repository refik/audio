from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi

class AkademiForm(ModelForm):
    class Meta:
        model = Bilgi
        exclude = ('mesaj',)

class TeklifForm(ModelForm):
    class Meta:
        model = Bilgi
        exclude = ('firma',)

class BultenForm(ModelForm):
    class Meta:
        model = Bilgi
        exclude = ('firma','mesaj',)

class IletisimForm(ModelForm):
    class Meta:
        model = Bilgi
        exclude = ('sehir','firma',)





