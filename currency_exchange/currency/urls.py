from django.urls import path
from . import views
from .views import CurrencyListView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'currency'



urlpatterns = [
    path('list/', CurrencyListView.as_view(), name='list'),
    path('exchange/', views.get_exchange_rates, name='exchange'),
    path('api-token-auth/', obtain_auth_token),

]
