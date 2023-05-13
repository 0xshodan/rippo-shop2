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
    photo = models.ImageField(upload_to="cars", blank=True)
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

    def __str__(self):
        mods = self.modifications.all()
        years_start = []
        years_end = []
        for mod in mods:
            years_start.append(mod.year_from)
            years_end.append(mod.year_end)
        return f"{self.name} ({min(years_start)} по {max(years_end)})"


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

    @property
    def years(self):
        years = ""
        if self.year_from == self.year_end:
            years = f"({self.year_from})"
        else:
            years = f"({self.year_from} по {self.year_end})"
        return years
    @property
    def fullname(self):
        name = self.car.car.brand.name + " " + self.car.car.name
        if self.car.name != self.name:
            name += " " + self.car.name + " " + self.name
        else:
            name += " " + self.name
        name += " " + self.years
        return name
    def __str__(self):
        return self.name + " " + self.years