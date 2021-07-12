from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя, удаляю поле username и делаю поле email ключевым."""

    email = models.EmailField(unique=True, blank=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
