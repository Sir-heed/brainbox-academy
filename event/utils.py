import json
import requests
from base64 import b64encode
from decouple import config

paystack_test_secret_key = config("paystack_test_secret_key")
paystack_test_headers = {"Authorization": f"Bearer {paystack_test_secret_key}"}


def initialize_transaction(email, amount, txref):
    url = 'https://api.paystack.co/transaction/initialize'
    payload = {
        "email": email, 
        "amount": amount * 100,
        "reference": txref,
        "callback_url": f'http://brainbox-academy.herokuapp.com/event/verify/{txref}'
    }
    r = requests.post(url, data=json.dumps(payload), headers=paystack_test_headers)
    print(r.json())
    if r.status_code == 200:
        res = r.json()
        return res
    else:
        return None


def verify_transaction(tx_ref):
    url = f'https://api.paystack.co/transaction/verify/{tx_ref}'
    r = requests.get(url, headers=paystack_test_headers)
    print(r.json())
    if r.status_code == 200:
        res = r.json()
        return res
    else:
        return None