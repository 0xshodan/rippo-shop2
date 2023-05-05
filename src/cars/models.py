from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Марка автомобиля", unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Модель авто")
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name="Бренд", related_name="cars"
    )

    class Meta:
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"
        ordering = ["name"]

    def __str__(self):
        return self.name


class CarGeneration(models.Model):
    name = models.CharField(max_length=150, verbose_name="Поколение автомобиля")
    slug = models.SlugField(unique=True)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="generations",
        verbose_name="Модель автомобиля",
    )

    class Meta:
        verbose_name = "Поколение автомобиля"
        verbose_name_plural = "Поколения автомобилей"


class CarModification(models.Model):
    name = models.CharField(max_length=200, verbose_name="Модификация авто")
    car = models.ForeignKey(
        CarGeneration,
        on_delete=models.CASCADE,
        related_name="modifications",
    )
    year_from = models.PositiveIntegerField(verbose_name="Год начала выпуска")
    year_end = models.PositiveIntegerField(verbose_name="Год конца выпуска")
    slug = models.SlugField(unique=True)
    spacers = models.ManyToManyField("spacers.Spacer")
