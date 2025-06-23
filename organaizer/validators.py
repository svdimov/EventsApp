from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OrganizerValidator:
    def __init__(self, message=None) -> None:
        self.message = message or "The company name is invalid!"

    def __call__(self, value: str, *args, **kwargs) -> None:

        for char in value:
            if not (char.isalpha() or char.isdigit() or char in [' ', '-']):
                raise ValidationError(self.message)

@deconstructible
class OrganizerSecretKeyValidator:
    def __init__(self, message=None) -> None:
        self.message = message or "Your secret key must have 4 unique digits!"

    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError(self.message)
        if len(value) != 4:
            raise ValidationError(self.message)