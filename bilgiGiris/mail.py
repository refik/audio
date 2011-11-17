# coding: utf-8
from ntlm.smtp import ntlm_authenticate
from audio.sifre import DOMAIN, PASSWORD
from audio.settings import GELISTIRME
import smtplib

def audiomail(kimden,kime,konu,mesaj):
    # Mail function shouldn't work on development machine.
    if GELISTIRME:
        return None

    server = smtplib.SMTP("mail.audio.com.tr")
    server.ehlo()
    ntlm_authenticate(server, DOMAIN, PASSWORD)
    fromaddr = kimden
    toaddrs  = kime
    message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (fromaddr, ", ".join(toaddrs),konu,mesaj))
    msg = unicode(message).encode("utf-8")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

