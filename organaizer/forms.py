
from django import forms

from organaizer.models import Organizer


class OrganizerBaseForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['company_name', 'phone_number', 'secret_key']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Enter a company name...'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter a valid phone number (digits only)...'
            }),
            'secret_key': forms.PasswordInput(attrs={
                'placeholder': 'Enter a secret key like <1234>...'
            }),
        }


class CreateOrganizerForm(OrganizerBaseForm):
    pass


class DeleteOrganizerForm(OrganizerBaseForm):
    pass


class DetailsOrganizerForm(OrganizerBaseForm):
    pass


class EditOrganizerForm(OrganizerBaseForm):
    class Meta:
        model = Organizer
        fields = ['company_name', 'phone_number', 'website']
        widgets = {
            'website': forms.TextInput(attrs={'placeholder': 'https//example.com'}),
        }


