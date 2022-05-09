from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator

from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, null=True)
    # avatar = models.ImageField(null=True, upload_to='profile/')
    avatar = CloudinaryField('profile', null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15, null=True)
    phone = models.CharField(max_length=15, unique=True)
    status = models.BooleanField(default=True)
    address = models.TextField(null=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def full_name(self):
        return self.get_full_name()

    def get_complete_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def __str__(self):
        return self.email


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.email


class Appointment(models.Model):
    APPOINTMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending', null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)