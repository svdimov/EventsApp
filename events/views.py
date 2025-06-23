from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from RegularExam.utils import get_user_object
from events.forms import CreateEventForm, DetailsEventForm, EditEventForm, DeleteEventForm
from events.models import Event


# Create your views here.
class DashboardEventView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_user_object()
        return context


class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create-event.html'
    success_url = reverse_lazy('dashboard')
    form_class = CreateEventForm

    def form_valid(self, form):
        form.instance.organizer = get_user_object()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_user_object()
        return context


class DetailsEventView(DetailView):
    model = Event
    template_name = 'events/details-event.html'
    form_class = DetailsEventForm
    success_url = reverse_lazy('dashboard')
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_user_object()
        return context


class EditEventView(UpdateView):
    model = Event
    template_name = 'events/edit-event.html'
    form_class = EditEventForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_user_object()
        return context


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'events/delete-event.html'
    form_class = DeleteEventForm
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_user_object()
        return context

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


    # def get_post(self):
    #     pass
    #
    # def form_invalid(self, form):
    #     return self.form_valid(form)





