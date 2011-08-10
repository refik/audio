from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

def temsilci(request):
    try:
        sorumlu = User.objects.filter(profile__sorumluSehir__isim__contains = request.GET['sehir'])
        temsilci = sorumlu[0]
        kisi = {'Isim' : temsilci.first_name + ' ' + temsilci.last_name, 'Telefon' : temsilci.profile.telefon, 'Email' : temsilci.email}
    except:
        kisi ={}
    return HttpResponse(json.dumps(kisi))    
