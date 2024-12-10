from django.urls import path
from . import views

urlpatterns = [
    path('exchange/', views.get_exchange_rates, name='exchange'),
]
