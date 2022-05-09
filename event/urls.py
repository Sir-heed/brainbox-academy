from django.urls import path, include
from django.conf.urls import handler404, handler500
from .views import event_details, event, add_event, event_payment, verify_event_payment

app_name = 'event'

urlpatterns = [
    path('', event, name='event'),
    path('add-event', add_event, name='add-event'),
    path('event-details/<int:pk>', event_details, name='event-details'),
    path('event-payment/<int:pk>', event_payment, name='event-payment'),
    path('verify/<str:ref_id>', verify_event_payment, name='verify-event-payment')
]