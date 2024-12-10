from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .external_api import get_exchange_rates

@csrf_exempt
def get_exchange_rates(request):
    if request.method == 'GET':
        try:
            rates = get_exchange_rates("USD")
            return JsonResponse({'rates': rates})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
