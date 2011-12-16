from django import template
from django.template.loader import render_to_string
from audio.teklif.forms import TeklifYapildiForm

register = template.Library()

@register.inclusion_tag('yapildi_liste.html')
def yapildi_listesi(teklif):
    yapilanlar = teklif.yapildi_set.all()
    return {'yapilanlar': yapilanlar, 'teklif': teklif}

@register.simple_tag(takes_context=True)
def yapildi_formu(context,instance):
    form = TeklifYapildiForm(initial={'kullanici':context['request'].user.pk, 'teklif': instance.pk})
    return render_to_string('yapildi_form.html', {'form': form}) 

