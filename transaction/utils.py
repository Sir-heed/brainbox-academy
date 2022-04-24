import requests
import json
from decouple import config

paystack_secret_key = config("paystack_secret_key")
paystack_headers = {"Authorization": f"Bearer {paystack_secret_key}"}

def initialize_transaction(email, amount, channels):
    url = 'https://api.paystack.co/transaction/initialize'
    payload = {
        "email": email, 
        "amount": amount * 100,
        "channels": [channels]
    }
    print(payload['channels'])
    r = requests.post(url, data=json.dumps(payload), headers=paystack_headers)
    print(r.json())
    if r.status_code == 200:
        res = r.json()
        return res
    else:
        return None


def verify_transaction(reference):
    url = f'https://api.paystack.co/transaction/verify/{reference}'
    r = requests.get(url, headers=paystack_headers)
    print(r.json())
    if r.status_code == 200:
        res = r.json()
        return res
    else:
        return None