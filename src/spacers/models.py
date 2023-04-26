from django.db import models


# Create your models here.
class Spacer(models.Model):
    article = models.CharField(max_length=20)
    CHOICES = ("Передние проставки", "Задние проставки")
    category = models.CharField(max_length=30, choices=CHOICES)
    description = models.CharField(max_length=2000, default="")
    price20mm = models.PositiveIntegerField()
    price30mm = models.PositiveIntegerField()
    price40mm = models.PositiveIntegerField()
    price50mm = models.PositiveIntegerField()
