from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Марки")
    slug = models.SlugField()


class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Модель авто")
    slug = models.SlugField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class CarYear(models.Model):
    name = models.CharField(max_length=150, verbose_name="Год выпуска")
    slug = models.SlugField()
    year_from = models.PositiveIntegerField()
    year_end = models.PositiveIntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class CarModification(models.Model):
    name = models.CharField(max_length=200, verbose_name="Модификация авто")
    car = models.ForeignKey(CarYear, on_delete=models.CASCADE)
    spacers = models.ManyToManyField("spacers.Spacer")
