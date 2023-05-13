from django.contrib import admin

from .models import Brand, Car, CarGeneration


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "name"]
    ordering = ("brand",)
    search_fields = ("name", "brand__name")


@admin.register(CarGeneration)
class CarGenerationAdmin(admin.ModelAdmin):
    list_display = ["get_brand", "get_car", "name"]
    ordering = ("car__brand__name",)
    search_fields = ("car__name", "car__brand__name")
    def get_brand(self, obj):
        return obj.car.brand

    def get_car(self, obj):
        return obj.car

    get_brand.admin_order_field = "name"
    get_brand.short_description = "Марка"
    get_car.admin_order_field = "name"
    get_car.short_description = "Модель"
