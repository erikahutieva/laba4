from fastapi import APIRouter, Depends, HTTPException
from ..models.currency import CurrencyExchange
from ..services.external_api import get_exchange_rate, get_supported_currencies
from ..services.security import get_current_user

router = APIRouter()

@router.get("/exchange/")
async def get_exchange_rate(currency_exchange: CurrencyExchange, current_user: str = Depends(get_current_user)):
    rate = get_exchange_rate(currency_exchange.from_currency, currency_exchange.to_currency)
    if rate is None:
        raise HTTPException(status_code=400, detail="Invalid currency codes")
    amount_in_target_currency = currency_exchange.amount * rate
    return {"from_currency": currency_exchange.from_currency, "to_currency": currency_exchange.to_currency, "amount": amount_in_target_currency}

@router.get("/list/")
async def get_supported_currencies(current_user: str = Depends(get_current_user)):
    return get_supported_currencies()

