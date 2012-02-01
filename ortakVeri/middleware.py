from django.http import HttpResponse
from audio.ortakVeri.mail import audiomail
import os
class CheckAssholeIP:
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR','YOK')
        if ip == '195.191.118.2' and not os.path.isfile('/home/refik/geldi'):
            os.system('touch /home/refik/geldi')
            audiomail('audioweb@audio.com.tr', ['refik.rfk@gmail.com'], 'asshole check', 'geldi kerata')
            return HttpResponse('<html><head><title>Audio Elektronik</title><script type="text/javascript">window.onload = function(){setTimeout(function(){open("http://www.audio.com.tr","_self");},6000);}</script></head><body><h1>Neyi kopyaladigimizi da yazsaymissin keske.</h1></h3><p>Bunun ne oldugu hakkinda bir fikriniz yoksa kusura bakmayin, sizin firmadan birisi bize sacma bir mesaj yollamis.</p></body></html>')
        else:
            return None
