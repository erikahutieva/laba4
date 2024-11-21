from django.db import models

# Create your models here.
# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Кастомная модель пользователя, основанная на AbstractUser.
    Вы можете добавить дополнительные поля, если потребуется.
    """
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="Email")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
