import string
import random
from .models import Transaction

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_transaction_reference(t_type):
    tx_ref = f'{t_type}_{get_random_string(7)}'
    while Transaction.objects.filter(reference=tx_ref).exists():
        tx_ref = f'{t_type}_{get_random_string(7)}'
    return tx_ref