from audio.haber.models import Haber
from django.views.generic import DetailView

class HaberView(DetailView):
    model = Haber
    template_name = 'haber.html'
    context_object_name = 'haber'

    def get_context_data(self, **kwargs):
        context = super(HaberView, self).get_context_data(**kwargs)
        context['butun_haberler'] = self.get_queryset()
        return context

    def get_object(self):
        if self.kwargs['slug'] == 'guncel':
            return Haber.objects.all()[0]
        else:
            return super(HaberView, self).get_object()
