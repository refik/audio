from audio.ortakVeri.models import Afis

def afis(request):
  afis = Afis.objects.all()
  return {'afis':afis}

