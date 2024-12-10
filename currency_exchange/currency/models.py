from django.db import models

# Create your models here.
# models.py
from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # Код валюты (например, USD, EUR)
    name = models.CharField(max_length=100)  # Полное название валюты (например, US Dollar, Euro)

    def __str__(self):
        return self.name
