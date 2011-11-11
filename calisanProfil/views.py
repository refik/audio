# coding: utf-8
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth import authenticate, login
import json

def temsilci(request):
    try:
        sorumlu = User.objects.filter(profile__sorumluSehir__isim__contains = request.GET['sehir'])
        temsilci = sorumlu.filter(profile__gorev__isim__contains = 'Temsilci')
        temsilci = temsilci[0]
        kisi = {'İsim' : temsilci.get_full_name(), 'Telefon' : temsilci.profile.telefon, 'Email' : temsilci.email}
    except:
        kisi ={}
    return HttpResponse(json.dumps(kisi))

