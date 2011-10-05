from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from audio.dokuman.models import Dokuman
import os, subprocess, threading

class cevrim(threading.Thread):
    def __init__(self,dosya,swfKlasor,sayfa):
        self.dosya = dosya
        self.swfKlasor = swfKlasor
        self.sayfa = sayfa
        threading.Thread.__init__ (self)
    def run(self):
        args = ['/usr/local/bin/pdf2swf', self.dosya.path, '-o', self.swfKlasor + '/' + '%d.swf'%self.sayfa, '-f', '-T', '9', '-t', '-p','%d'%self.sayfa, '-s','storeallcharacters']
        p = subprocess.Popen(args,stdout=subprocess.PIPE)
        #print self.sayfa, 'ilk deneme'
        for line in iter(p.stdout.readline,''):
            if line[:5] == 'ERROR':
                args += ['-s','poly2bitmap']
                subprocess.Popen(args)
                #print self.sayfa, 'ikinci deneme'

def dokuman(request,isim):
    dokuman = get_object_or_404(Dokuman, slug=isim)
    dosya = dokuman.dosya
    klasor = dosya.filename_root + '-katalog-gorunumu-dosyalari'
    swfKlasor = os.path.dirname(dosya.path) + '/' + klasor
    if not os.path.exists(swfKlasor):
        os.mkdir(swfKlasor)
        s_p = subprocess.Popen(['pdfinfo','-meta',dosya.path],stdout=subprocess.PIPE)
        #print type(int(s_p.stdout.readlines()[6].rstrip().split(' ')[-1]))
        sayfa = int(s_p.stdout.readlines()[6].rstrip().split(' ')[-1])
        for i in range(1,sayfa+1):
            cevrim(dosya,swfKlasor,i).start()
        return HttpResponse('Belgeniz Katalog Formuna Cevriliyor, 5 Dakika Sonra Tekrar Gelin')
    swfListe = os.listdir(swfKlasor)
    swfListe.sort(key=lambda f:int(f[:-4]),reverse=True)
    sayfaSayi = swfListe[0][:-4]
    swfUrl =  os.path.dirname(dosya.url) + '/' + klasor
    return render_to_response('dokuman.html', {'dokuman':dokuman, 'sayfa':sayfaSayi, 'swfUrl':swfUrl})    
