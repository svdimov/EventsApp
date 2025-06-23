# TODO organaizer -> This field should remain hidden in forms.
from django import forms
from django.utils import timezone

from events.models import Event


class BaseEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('organizer',)

        widgets = {
            'slogan': forms.TextInput(attrs={'placeholder': 'Provide an appealing text...'}),
            'location': forms.TextInput(),
            'start_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'value': timezone.now().strftime('%Y-%m-%dT%H:%M')}),
            'available_tickets': forms.NumberInput(),
            'key_features': forms.Textarea(attrs={'placeholder': 'Provide important event details...'}),
            'banner_url': forms.URLInput(attrs={'placeholder': 'An optional banner image URL...'}),
        }
        labels = {
            'start_time': 'Event Date/Time:',
            'key_features': 'Event Key Features:',
            'banner_url': 'Event Banner URL:',
            'available_tickets': 'Available Tickets:',
        }
class CreateEventForm(BaseEventForm):
    pass


class EditEventForm(BaseEventForm):
    pass


class DeleteEventForm(BaseEventForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

class DetailsEventForm(forms.ModelForm):
    pass
