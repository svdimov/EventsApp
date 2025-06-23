from organaizer.models import Organizer


def get_user_object():
    return Organizer.objects.first()
