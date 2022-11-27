from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Birthday(models.Model):
    birthday = models.DateTimeField(
        null=True,
        verbose_name="День рождения"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
