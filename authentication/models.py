from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, null=True)
    avatar = models.ImageField(null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15, null=True)
    phone = models.CharField(max_length=15, unique=True)
    status = models.BooleanField(default=True)
    address = models.TextField(null=True)

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

