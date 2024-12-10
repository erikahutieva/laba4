import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')
import django
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase

# Указываем путь к настройкам проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')
 # Путь к вашему settings.py

# Настроим Django
django.setup()

class AuthTests(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Задаем URL для логина (замените на правильный URL)
        self.login_url = reverse('auth:login')  # Замените на правильный URL для вашего проекта

    def test_login_success(self):
        # Пытаемся выполнить запрос на логин
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        # Проверяем, что код ответа успешный
        self.assertEqual(response.status_code, 200)
        # Проверяем, что на странице есть текст "Welcome" (замените на корректный для вашего проекта)
        self.assertContains(response, 'Welcome')

    def test_login_failure(self):
        # Пытаемся выполнить запрос с неправильными данными
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        # Проверяем, что код ошибки 401 (или тот, который ожидаете)
        self.assertEqual(response.status_code, 401)
