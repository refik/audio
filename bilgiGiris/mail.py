from ntlm.smtp import ntlm_authenticate
import smtplib

def audiomail(kimden,kime,konu,mesaj):
    server = smtplib.SMTP("mail.audio.com.tr")
    server.ehlo()
    ntlm_authenticate(server, r"audio\audioweb", "4455")
    fromaddr = kimden
    toaddrs  = kime
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (fromaddr, ", ".join(toaddrs),konu,mesaj))
    server.sendmail(fromaddr, toaddrs, unicode(msg))
    server.quit()
