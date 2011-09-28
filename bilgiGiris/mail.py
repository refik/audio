# coding: utf-8
from ntlm.smtp import ntlm_authenticate
import smtplib

def audiomail(kimden,kime,konu,mesaj):
    server = smtplib.SMTP("mail.audio.com.tr")
    server.ehlo()
    ntlm_authenticate(server, r"audio\audioweb", "4455")
    fromaddr = kimden
    toaddrs  = kime
    message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (fromaddr, ", ".join(toaddrs),konu,mesaj))
    msg = unicode(message).encode("utf-8")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

