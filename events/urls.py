from django.urls import path

from events import views
from events.views import DetailsEventView, EditEventView, DeleteEventView

urlpatterns = [
    path('events/', views.DashboardEventView.as_view(), name='dashboard'),
    path('events/create/', views.CreateEventView.as_view(), name='create-event'),
    path('events/<int:pk>/details/', DetailsEventView.as_view(), name='event-details'),
    path('events/<int:pk>/edit/', EditEventView.as_view(), name='event-edit'),
    path('events/<int:pk>/delete/', DeleteEventView.as_view(), name='event-delete'),

]

