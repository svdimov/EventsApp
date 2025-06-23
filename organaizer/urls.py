from django.urls import path

from organaizer.views import CreateOrganizerView, DetailsOrganizerView, EditOrganizerView, DeleteOrganizerView

urlpatterns = [
    path('organizer/create/', CreateOrganizerView.as_view(), name='create-organizer'),
    path('organizer/details/', DetailsOrganizerView.as_view(), name='details-organizer'),
    path('organizer/edit/', EditOrganizerView.as_view(), name='edit-organizer'),
    path('organizer/delete/', DeleteOrganizerView.as_view(), name='delete-organizer'),
]