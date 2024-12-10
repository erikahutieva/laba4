# external_api.py
import requests
from django.conf import settings

BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_exchange_rates(base_currency="USD"):
    response = requests.get(f"{BASE_URL}{base_currency}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching exchange rates")
