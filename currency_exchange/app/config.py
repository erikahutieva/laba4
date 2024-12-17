from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    
    secret_key: str = os.getenv("SECRET_KEY", "default_secret_key")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    api_key: str = os.getenv("API_KEY", "https://api.exchangerate-api.com/v4/latest/USD")

settings = Settings()
