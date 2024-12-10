# tests/test_auth.py
from django.test import TestCase
from rest_framework.test import APIClient

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        response = self.client.post('/auth/register/', {"username": "test", "password": "123456"})
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.client.post('/auth/register/', {"username": "test", "password": "123456"})
        response = self.client.post('/auth/login/', {"username": "test", "password": "123456"})
        self.assertEqual(response.status_code, 200)
