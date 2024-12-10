from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .security import create_jwt

users = {}  # Используем простой словарь вместо базы данных

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

users = {}  # Используем простой словарь вместо базы данных

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            if username in users:
                return JsonResponse({'error': 'User already exists'}, status=400)
            users[username] = password
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if username in users and users[username] == password:
            token = create_jwt({'username': username})
            return JsonResponse({'token': token})
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
