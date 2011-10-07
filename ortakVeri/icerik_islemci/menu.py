from audio.ortakVeri.models import Menu

def menu(request):
  menu = Menu.objects.all()
  return {'menu' : menu}

