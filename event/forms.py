from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        read_only_fields = ['created_by', 'time_created', 'date_created', 'last_updated']
        fields = '__all__'