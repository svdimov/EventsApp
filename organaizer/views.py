from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from RegularExam.utils import get_user_object
from organaizer.forms import OrganizerBaseForm, CreateOrganizerForm, DetailsOrganizerForm, EditOrganizerForm, \
    DeleteOrganizerForm
from organaizer.models import Organizer


# Create your views here.

class CreateOrganizerView(CreateView):
    model = Organizer
    form_class = CreateOrganizerForm
    success_url = reverse_lazy('dashboard')
    template_name = 'organaizer/create-organizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_user_object()
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)

class DetailsOrganizerView(DetailView):
    model = Organizer
    form_class = DetailsOrganizerForm
    context_object_name = 'organizer'
    template_name = 'organaizer/details-organizer.html'

    def get_object(self, queryset=None):
        return get_user_object()

class EditOrganizerView(UpdateView):
    model = Organizer
    form_class = EditOrganizerForm
    template_name = 'organaizer/edit-organizer.html'
    success_url = reverse_lazy('details-organizer')

    def get_object(self, queryset=None):
        return get_user_object()


class DeleteOrganizerView(DeleteView):
    model = Organizer
    template_name = 'organaizer/delete-organizer.html'
    form_class = DeleteOrganizerForm
    success_url = reverse_lazy('home')


    def get_object(self, queryset = None):
        return get_user_object()

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
