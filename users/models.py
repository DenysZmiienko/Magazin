from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username


    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'