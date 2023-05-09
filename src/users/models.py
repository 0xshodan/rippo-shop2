from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    discount = models.PositiveSmallIntegerField(default=0,verbose_name="Персональная скидка покупателя в процентах")

