from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
import json

# Пример функции для получения обменных курсов
def get_exchange_rates(from_currency, to_currency):
    # Тут должен быть реальный запрос к API или логика вычисления курса
    # В данном примере курс будет статичным для демонстрации
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75},
        'EUR': {'USD': 1.18, 'GBP': 0.88},
        'GBP': {'USD': 1.33, 'EUR': 1.14},
    }
    try:
        return exchange_rates[from_currency][to_currency]
    except KeyError:
        raise ValidationError("Invalid currency code.")

# Новый DRF представление для получения курсов
class CurrencyListView(APIView):
    permission_classes = [IsAuthenticated]  # Требуется аутентификация

    def post(self, request):
        try:
            data = request.data
            amount = data.get("amount")
            from_currency = data.get("from_currency")
            to_currency = data.get("to_currency")

            # Проверка обязательных параметров
            if not amount or not from_currency or not to_currency:
                raise ValidationError("Amount, from_currency, and to_currency are required.")

            # Получаем обменный курс
            exchange_rate = get_exchange_rates(from_currency, to_currency)
            converted_amount = amount * exchange_rate

            # Возвращаем ответ в формате JSON
            return Response({
                "converted_amount": converted_amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "exchange_rate": exchange_rate
            })

        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
