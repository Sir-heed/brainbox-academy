from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
from .utils import custom_normalize_email

class CustomUserManager(BaseUserManager):
    """
    Custom user model managers where username is the unique identifiers
    for authentication instead of username
    """

    def create_user(self, email, password=None, active=False, admin=False, staff=False):
        if not email:
            raise ValueError("Users must have an email address")
        # user_obj = self.model(email=self.normalize_email(email))
        user_obj = self.model(email=custom_normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = staff
        user_obj.admin = admin
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, password, username=None, **extra_fields):
        """
        Create and save a Superuser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)