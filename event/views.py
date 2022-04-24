from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib import messages

from .forms import EventForm

from .models import Event

# Create your views here.
def event(request):
    template = loader.get_template('event/event.html')
    events = Event.objects.all()
    paginator = Paginator(events, 10) # Show 25 news per page.
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)
    context = {
        'events': events
    }
    return HttpResponse(template.render(context, request))


def add_event(request):
    template = loader.get_template('event/add-event.html')
    context = {}
    print(request.POST)
    form = EventForm(request.POST or None)
    print(form.is_valid)
    print(form.errors)
    if form.is_valid():
        event = form.save()
        messages.success(request, "Event created successful.")
        return redirect("event:event")
    context['form']= form
    return HttpResponse(template.render(context, request))

    
def event_details(request, pk):
    template = loader.get_template('event/event-details.html')
    event = Event.objects.get(id=pk)
    context = {
        'event': event
    }
    return HttpResponse(template.render(context, request))