from django.shortcuts import render
from django.views.generic import TemplateView

from RegularExam.utils import get_user_object
from organaizer.models import Organizer


# Create your views here.
class HomePageView(TemplateView):
    model = Organizer
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['organizer'] = get_user_object()
        return context