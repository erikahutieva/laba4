from pydantic import BaseModel

class CurrencyExchange(BaseModel):
    from_currency: str
    to_currency: str
    amount: float = 1
