from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib import messages
from event.helpers import generate_transaction_reference

from event.utils import initialize_transaction, verify_transaction

from .forms import EventForm

from .models import Event, Transaction

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


def event_payment(request, pk):
    try:
        event = Event.objects.get(id=pk)
        if event.status not in ['Upcoming', 'On-Going']:
            messages.error(request, "Event is not available")
            return redirect(reverse('event:event-details', kwargs={"pk": event.id}))
        else:
            amount = event.price
            reference = generate_transaction_reference('event')
            paystact_init = initialize_transaction(request.user.email, amount, reference)
            if paystact_init is not None:
                Transaction.objects.create(
                    amount = amount,
                    user = request.user,
                    event = event,
                    transaction_type = 'event',
                    status = 'pending',
                    reference = reference,
                    paystack_ref = paystact_init['data']['reference']
                )
                return redirect(paystact_init['data']['authorization_url'])
            else:
                messages.error(request, "Transaction failed")
                return redirect(reverse('event:event-details', kwargs={"pk": event.id}))
    except Event.DoesNotExist:
        messages.error(request, "Event does not exist")
        return redirect("event:event")


def verify_event_payment(request, ref_id):
    try:
        txn = Transaction.objects.get(reference=ref_id)
        verify_txn = verify_transaction(ref_id)
        if verify_txn is not None:
            if verify_txn['data']['status'] == 'success':
                txn.status = 'success'
                txn.authorization_code = verify_txn['data']['authorization']['authorization_code']
                txn.save()
                return redirect("event:event")
            else:
                return redirect("event:event")
        else:
            return redirect("event:event")
    except Transaction.DoesNotExist:
        return redirect("event:event")