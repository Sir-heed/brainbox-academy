from django.db import models

from authentication.models import User, Tutor

# Create your models here.
class Event(models.Model):
    EVENT_STATUS = (
        ('On-Going', 'On-Going'),
        ('Ended', 'Ended'),
        ('Upcoming', 'Upcoming'),
        ('Cancelled', 'Cancelled')
    )
    topic = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='event_created_by')
    tutors = models.ManyToManyField(Tutor)
    participants = models.ManyToManyField(User, blank=True)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    duration_in_hours = models.IntegerField()
    status = models.CharField(max_length=20, choices=EVENT_STATUS, default='Upcoming')
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.topic


# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('event','event'),
    )
    amount = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    transfer_code = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=20, null=True, blank=True)
    authorization_code = models.CharField(max_length=20, null=True, blank=True)
    paystack_ref = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class WebhookTransaction(models.Model):
    event = models.CharField(max_length=50, null=True, blank=True)
    transfer_code = models.CharField(max_length=50, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    transfer_recipient = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)