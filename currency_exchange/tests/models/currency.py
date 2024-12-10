# models/currency.py

from pydantic import BaseModel

class CurrencyExchange(BaseModel):
    from_currency: str  # Валюта, из которой происходит обмен
    to_currency: str    # Валюта, в которую происходит обмен
    amount: float = 1   # Сумма для обмена, по умолчанию 1

    class Config:
        orm_mode = True
