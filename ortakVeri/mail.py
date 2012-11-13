# coding: utf-8
from ntlm.smtp import ntlm_authenticate
from audio.sifre import DOMAIN, PASSWORD
from audio.settings import GELISTIRME
from django.utils.encoding import smart_str
import smtplib

def audiomail(kimden,kime,konu,mesaj):
    konu = smart_str(konu)
    mesaj = smart_str(mesaj)
    kime = map(smart_str, kime)
    kimden = smart_str(kimden)

    # Mail function shouldn't work on development machine.
    if GELISTIRME:
        print kimden, kime, konu, mesaj
        return None

    server = smtplib.SMTP("mail.audio.com.tr", port=587)
    server.ehlo()
    ntlm_authenticate(server, DOMAIN, PASSWORD)
    fromaddr = kimden
    toaddrs  = kime
    message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (fromaddr, ", ".join(toaddrs),konu,mesaj))
    msg = unicode(message).encode("utf-8")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

