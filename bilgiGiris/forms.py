from django.forms import ModelForm
from audio.bilgiGiris.models import Bilgi

class TeklifForm(ModelForm):
    TEMPLATE = 'bilgiGiris/teklif.html'
    class Meta:
        model = Bilgi
        exclude = ('firma',)

class AkademiForm(ModelForm):
    TEMPLATE = 'bilgiGiris/akademi.bulten.iletisim.html'
    class Meta:
        model = Bilgi
        exclude = ('mesaj',)

class BultenForm(ModelForm):
    TEMPLATE = 'bilgiGiris/akademi.bulten.iletisim.html'
    class Meta:
        model = Bilgi
        exclude = ('firma','mesaj',)

class IletisimForm(ModelForm):
    TEMPLATE = 'bilgiGiris/akademi.bulten.iletisim.html'
    class Meta:
        model = Bilgi
        exclude = ('sehir','firma',)





