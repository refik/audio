# coding: utf-8
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth import authenticate, login
import json
import random

def temsilci(request):
    try:
        temsilci = User.objects.filter(profile__ikincil=True,profile__sorumluSehir__isim__contains = request.GET['sehir'])
        if not temsilci:
            temsilci = User.objects.filter(profile__birincil=True,profile__sorumluSehir__isim__contains = request.GET['sehir'])
        temsilci = random.choice(temsilci)
        kisi = {'İsim' : temsilci.get_full_name(), 'Telefon' : temsilci.profile.telefon, 'Email' : temsilci.email}
    except:
        kisi ={}
    return HttpResponse(json.dumps(kisi))

