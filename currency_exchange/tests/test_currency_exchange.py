import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')
import django
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

# Указываем путь к настройкам проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')
 # Путь к вашему settings.py

# Настроим Django
django.setup()

# Тест для обмена валют
class CurrencyExchangeTests(TestCase):
    def setUp(self):
        # Здесь можно создать тестовые данные для валют и курсов
        pass

    def test_currency_exchange_success(self):
        # Замените '/currency/exchange/' на ваш фактический URL
        response = self.client.post(reverse('currency:list'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["converted_amount"], 85.0)  # Предположим, что курс 1 USD = 0.85 EUR
        self.assertEqual(data["from_currency"], "USD")
        self.assertEqual(data["to_currency"], "EUR")

    def test_currency_exchange_invalid_currency(self):
        # Замените '/currency/exchange/' на ваш фактический URL
        from rest_framework.test import APIClient
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token 7eb405fdae5edf2136dda5cb873ce644052b678b')
        response = client.post(reverse('currency:list'), data)
        response = self.client.post(reverse('currency:exchange'), json={
            "from_currency": "XYZ",
            "to_currency": "ABC",
            "amount": 100
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())
