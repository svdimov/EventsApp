from django.core.validators import MinLengthValidator
from django.db import models

from organaizer.validators import OrganizerValidator, OrganizerSecretKeyValidator


# Create your models here.
class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        help_text="*Allowed names contain letters, digits, spaces, and hyphens." ,
        validators=[
            MinLengthValidator(2),
            OrganizerValidator()
        ])

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        error_messages={'unique':"That phone number is already in use!"}
    )
    secret_key  = models.CharField(
        max_length=4,
        validators=[
            OrganizerSecretKeyValidator(),
            MinLengthValidator(4),
        ],
        help_text="*Pick a combination of 4 unique digits."

    )
    website = models.URLField(
        blank=True,
        null=True,
    )

