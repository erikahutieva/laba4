from django.test import TestCase

# Create your tests here.
# api/tests.py
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def test_register(self):
        response = self.client.post('/auth/register/', {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        User.objects.create_user(username='testuser', password='testpass')
        response = self.client.post('/auth/login/', {'username': 'testuser', 'password': 'testpass'})
        self.assertIn('access', response.data)
