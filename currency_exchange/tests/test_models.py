import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')

import django
from pydantic import ValidationError
from models.currency import CurrencyExchange  # Убедитесь, что путь правильный

# Указываем путь к настройкам проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')
  # Путь к вашему settings.py

# Настроим Django
django.setup()

def test_currency_exchange_model_valid():
    data = {
        "from_currency": "USD",
        "to_currency": "EUR",
        "amount": 100
    }
    model = CurrencyExchange(**data)
    assert model.from_currency == "USD"
    assert model.to_currency == "EUR"
    assert model.amount == 100

def test_currency_exchange_model_invalid():
    data = {
        "from_currency": "USD",
        "to_currency": "EUR",
        "amount": -100  # Отрицательное значение должно вызвать ошибку
    }
    try:
        model = CurrencyExchange(**data)
    except ValidationError as e:
        # Проверяем, что ошибка соответствует ожиданиям
        assert e.errors()[0]["msg"] == "ensure this value is greater than or equal to 0"
