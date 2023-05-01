from django.db import models


# Create your models here.
class Spacer(models.Model):
    article = models.CharField(max_length=20)
    CHOICES = (
        ("Передние проставки", "Передние проставки"),
        ("Задние проставки", "Задние проставки"),
    )
    category = models.CharField(
        max_length=30, choices=CHOICES, default="Передние проставки"
    )
    description = models.CharField(max_length=2000, default="")
    mount = models.CharField(max_length=200, default="")
    price20mm = models.PositiveIntegerField(default=0)
    price30mm = models.PositiveIntegerField(default=0)
    price40mm = models.PositiveIntegerField(default=0)
    price50mm = models.PositiveIntegerField(default=0)
