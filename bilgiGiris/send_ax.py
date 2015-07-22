# coding: utf-8
import json
import os
import threading
import logging
from audio.bilgiGiris.models import Bilgi
from audio.ortakVeri.mail import audiomail
from pysimplesoap.client import SoapClient, SoapFault

AX_QUEUE_FOLDER = '/home/refik/ax-queue'

class SendThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        _send_ax()

def send_ax():
    SendThread().start()

def _send_ax():
    client = SoapClient('http://uzak.audio.com.tr:88/AxIntegrations/AxService.asmx', action='http://tempuri.org/', namespace='http://tempuri.org/', ns='tem')
    files = os.listdir(AX_QUEUE_FOLDER) 
    for name in files:
        try:
            path = os.path.join(AX_QUEUE_FOLDER, name)
            with open(path, 'r') as infile:
                data = json.load(infile)
            #data = dict([(k.encode('utf8'), v.encode('utf8')) for k, v in data.items()])
            bilgi = Bilgi.objects.get(pk=int(name))
            if bilgi.ax_code:
                raise Exception('Teklif %s already has an ax_code: %s, no duplicate allowed. %s' % (name, bilgi.ax_code, bilgi.tarih))
            resp = client.call('AddWebQuotationForm', **data)
            ax_code = str(resp.AddWebQuotationFormResult) 
            bilgi.ax_code = ax_code
            bilgi.save()
        except Exception as e:
            if isinstance(e, SoapFault) and e.faultcode == 'soap:Server':
                body = "%s\n\nRequest:\n\n%s\n\n\nResponse:\n\n%s\n" % (unicode(e).encode('utf8'), client.xml_request, client.xml_response)
                subject = 'Web Teklif Axapta Server Hatasi'
                audiomail('audioweb@audio.com.tr', ['ibrahimbulbul@audio.com.tr '], subject, body)
                audiomail('audioweb@audio.com.tr', ['refik.rfk@gmail.com'], subject, body)
            logging.exception('hello')
        else:
            os.unlink(path)
