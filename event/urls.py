from django.urls import path, include
from django.conf.urls import handler404, handler500
from .views import event_details, event, add_event

app_name = 'event'

urlpatterns = [
    path('', event, name='event'),
    path('add-event', add_event, name='add-event'),
    path('event-details/<int:pk>', event_details, name='event-details'),
]