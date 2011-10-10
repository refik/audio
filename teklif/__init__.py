# coding: utf-8
from audio.teklif.forms import TeklifYorumFormu
from audio.teklif.models import TeklifYorum

def get_model():
    return TeklifYorum

def get_form():
    return TeklifYorumFormu
