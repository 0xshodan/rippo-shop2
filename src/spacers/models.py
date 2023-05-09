from django.db import models


# Create your models here.
class Spacer(models.Model):
    article = models.CharField(max_length=20, verbose_name="Артикул")
    CHOICES = (
        ("Передние проставки", "Передние проставки"),
        ("Задние проставки", "Задние проставки"),
    )
    category = models.CharField(
        max_length=30, choices=CHOICES, default="Передние проставки", verbose_name="Тип проставок"
    )
    photo = models.ImageField(upload_to="spacers", blank=True, verbose_name="Фото")
    description = models.CharField(max_length=2000, default="", verbose_name="Комментарий")
    mount = models.CharField(max_length=200, default="", verbose_name="Примечание к установке")
    price20mm = models.PositiveIntegerField(default=0, verbose_name="Цена 20мм")
    price30mm = models.PositiveIntegerField(default=0, verbose_name="Цена 30мм")
    price40mm = models.PositiveIntegerField(default=0, verbose_name="Цена 40мм")
    price50mm = models.PositiveIntegerField(default=0, verbose_name="Цена 50мм")

    class Meta:
        verbose_name = "Проставка"
        verbose_name_plural = "Проставки"
