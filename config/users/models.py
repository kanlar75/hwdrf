from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    town = models.CharField(max_length=150, **NULLABLE, verbose_name='город')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

