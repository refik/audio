from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import HttpResponse
from django.template import RequestContext
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from audio.dokuman.models import Dokuman
from audio.settings import STATIC_URL
from pyPdf import PdfFileReader
import subprocess
import threading
import os

def dokuman(request, isim):
    dokuman = get_object_or_404(Dokuman, slug=isim)
    dosya = dokuman.dosya
    klasor = dosya.filename_root + '-katalog-gorunumu-dosyalari'
    swfKlasor = os.path.dirname(dosya.path) + '/' + klasor
    sayfaSayi = len(default_storage.listdir(swfKlasor)[1])
    swfUrl =  STATIC_URL + swfKlasor
    return render_to_response('dokuman.html', 
                              {'dokuman':dokuman, 
                               'sayfa':sayfaSayi, 
                               'swfUrl':swfUrl},
                              context_instance = RequestContext(request))
