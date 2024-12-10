import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение секретного ключа из переменной окружения
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Функция для создания JWT
def create_jwt(user_data):
    payload = {
        "user_data": user_data,  # данные пользователя (например, username)
        "exp": datetime.utcnow() + timedelta(hours=1)  # срок действия токена
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Функция для декодирования JWT
def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None  # Если токен истек
    except jwt.InvalidTokenError:
        return None  # Если токен недействителен
