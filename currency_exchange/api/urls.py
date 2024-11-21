# api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .views import ExchangeRateView, ConvertCurrencyView, SupportedCurrenciesView


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class ExchangeRateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        if response.status_code == 200:
            return Response(response.json())
        return Response({"error": "Failed to fetch exchange rates"}, status=response.status_code)

class ConvertCurrencyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        base = request.data.get('base')
        target = request.data.get('target')
        amount = float(request.data.get('amount', 1))
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{base}')
        if response.status_code == 200:
            rates = response.json().get('rates', {})
            if target in rates:
                converted = amount * rates[target]
                return Response({"converted_amount": converted})
        return Response({"error": "Conversion failed"}, status=400)

class SupportedCurrenciesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        if response.status_code == 200:
            rates = response.json().get('rates', {})
            return Response({"currencies": list(rates.keys())})
        return Response({"error": "Failed to fetch currencies"}, status=400)



urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('currency/exchange/', ExchangeRateView.as_view(), name='exchange_rate'),
    path('currency/convert/', ConvertCurrencyView.as_view(), name='convert_currency'),
    path('currency/list/', SupportedCurrenciesView.as_view(), name='supported_currencies'),
]
