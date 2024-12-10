# schemas.py
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)

class CurrencyConversion(BaseModel):
    from_currency: str
    to_currency: str
    amount: float = 1.0
