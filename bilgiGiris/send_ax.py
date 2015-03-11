# coding: utf-8
import json
import os
import threading
import logging
from audio.bilgiGiris.models import Bilgi
from pysimplesoap.client import SoapClient

logging.basicConfig(level=logging.DEBUG)
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
            resp = client.call('AddWebQuotationForm', **data)
            ax_code = str(resp.AddWebQuotationFormResult) 
            bilgi = Bilgi.objects.get(pk=int(name))
            bilgi.ax_code = ax_code
            bilgi.save()
        except:
            logging.exception('hello')
        else:
            os.unlink(path)
