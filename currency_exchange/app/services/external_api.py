import requests
from ..config import settings

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if to_currency in data["rates"]:
            return data["rates"][to_currency]
    return None

def get_supported_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"]
    return {}
