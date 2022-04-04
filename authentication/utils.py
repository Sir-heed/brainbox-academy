import re
import random
import string
from django.core.exceptions import ValidationError as FieldValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    pattern = re.compile(r"^\+?1?\d{9,15}$")
    if not bool(pattern.match(value)):
        raise FieldValidationError(
            _(
                "Invalid! Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),
            params={"value": value},
        )

def custom_normalize_email(email):
    return email.strip().lower()


def get_random_string(length):
    # choose from all letter and digits
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def admin_check(user):
    return user.groups.filter(name='admin') and user.is_active