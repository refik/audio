from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from audio.teklif.models import Teklif, Durum
from audio.ortakVeri.mail import audiomail
import datetime

# A management command to check whether there is any offer to unfreeze
# and if there is, send a notification to owner
class Command(BaseCommand):
    help = 'Checks if there is an offer that should be unfreezed'

    def handle(self, *args, **kwargs):
        freeze_status = Durum.objects.get(isim__contains='donduruldu')
        today = datetime.date.today()
        for teklif in Teklif.objects.filter(durum__isim__contains='donduruldu'):
            # Finding out until when the offer is freezed
            freezed_by = teklif.yapildi_set.filter(durum=freeze_status)[0]
            freeze_until = freezed_by.dondur
            
            if(today >= freeze_until):
                try:
                    # Check if a previous action exists with an entered status
                    previous_status = teklif.yapildi_set.exclude(Q(durum=freeze_status) | Q(durum=None))[0].durum
                except:
                    # If none found set it to 'eylem yapilmadi' (no action) status
                    previous_status = Durum.objects.get(pk=1)

                representative = teklif.temsilci
                teklif.durum = previous_status
                teklif.save()

                audiomail('audioweb@audio.com.tr', [representative.email], 'Dondurulan teklif acildi',
"""Sayin %s,

%s tarihinde dondurdugunuz #%d numarali teklifiniz, bugun acilmistir. Bu teklifi dondururken yazdiginiz
aciklama mesaji: %s. 

Teklifin detaylari icin: %s

Iyi calismalar
"""             % (representative.get_full_name(), freezed_by.tarih.strftime('%d/%m/%y'), 
                   teklif.pk, freezed_by.mesaj, teklif.get_absolute_url()))


