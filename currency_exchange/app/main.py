from fastapi import FastAPI
from .routes import auth, currency

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(currency.router, prefix="/currency", tags=["currency"])
