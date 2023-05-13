from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import View

from .models import Brand, Car, CarGeneration, CarModification


class TestView(View):
    def get(self, request):
        return JsonResponse({"ok": True})


# PAGES
class BrandsView(View):
    def get(self, request, slug):
        brand = Brand.objects.get(slug=slug)
        template = loader.get_template("cars.html")
        context = {"cars": brand.cars.all(), "url": "car", "brand": brand}
        return HttpResponse(template.render(context, request))


class CarsView(View):
    def get(self, request, slug):
        car = Car.objects.get(slug=slug)
        generations = car.generations.all()
        if len(generations) == 1:
            if car.name == generations[0].name:
                view = GenerationView()
                resp = view.get(request, generations[0].slug)
                return resp
        template = loader.get_template("cars.html")
        context = {
            "cars": generations,
            "url": "generation",
            "brand": car.brand,
            "car": car,
        }
        return HttpResponse(template.render(context, request))


class GenerationView(View):
    def get(self, request, slug):
        car = CarGeneration.objects.get(slug=slug)
        modifications = car.modifications.all()
        if len(modifications) == 1:
            if car.name == modifications[0].name:
                view = ModificationView()
                resp = view.get(request, modifications[0].slug)
                return resp
        template = loader.get_template("cars.html")
        context = {
            "cars": modifications,
            "url": "modification",
            "brand": car.car.brand,
            "car": car.car,
            "generation": car,
        }
        return HttpResponse(template.render(context, request))


class ModificationView(View):
    def get(self, request, slug):
        car = CarModification.objects.get(slug=slug)
        template = loader.get_template("spacers.html")
        priorities = {"Передние проставки": 1, "Задние проставки":2, "Удлинитель заднего амортизатора":3}
        spacers = []
        for spacer in car.spacers.all():
            spacer.priority = priorities[spacer.category]
            spacers.append(spacer)
        spacers = sorted(spacers, key=lambda x: x.priority)
        context = {
            "spacers": spacers,
            "brand": car.car.car.brand,
            "car": car.car.car,
            "generation": car.car,
            "modification": car,
        }
        return HttpResponse(template.render(context, request))


# FOR AJAX (для виджета быстрый подбор проставок)
class CarApiView(View):
    def get(self, _, brand_id: int) -> JsonResponse:
        try:
            brand = Brand.objects.get(pk=brand_id)
        except Brand.DoesNotExist:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Brand with id: {brand_id} does not exist",
                }
            )
        ret = []
        for car in brand.cars.all():
            ret.append({"id": car.pk, "name": car.name, "slug": car.slug})
        return JsonResponse({"error": False, "cars": ret})


class CarGenerationApiView(View):
    def get(self, _, car_id: int) -> JsonResponse:
        try:
            car = Car.objects.get(pk=car_id)
        except CarGeneration.DoesNotExist:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Car with id: {car_id} does not exist",
                }
            )
        ret = []
        for generation in car.generations.all():
            ret.append(
                {
                    "id": generation.pk,
                    "name": str(generation),
                    "slug": generation.slug,
                }
            )
        print(ret)
        return JsonResponse({"error": False, "cars": ret})


class CarModificationApiView(View):
    def get(self, _, car_id: int) -> JsonResponse:
        try:
            car = CarGeneration.objects.get(pk=car_id)
        except Car.DoesNotExist:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Car with id: {car_id} does not exist",
                }
            )
        ret = []
        for modification in car.modifications.all():
            ret.append(
                {
                    "id": modification.pk,
                    "name": str(modification),
                    "slug": modification.slug,
                }
            )

        return JsonResponse({"error": False, "cars": ret})


# FOR AJAX (для кнопки подбор)
class GetBrandSlugView(View):
    def get(self, _, brand_id: int) -> JsonResponse:
        try:
            brand = Brand.objects.get(pk=brand_id)
        except:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Brand with id: {brand_id} does not exist",
                }
            )
        return JsonResponse({"error": False, "slug": brand.slug})


class GetCarSlugView(View):
    def get(self, _, car_id: int) -> JsonResponse:
        try:
            car = Car.objects.get(pk=car_id)
        except:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Car with id: {car_id} does not exist",
                }
            )
        return JsonResponse({"error": False, "slug": car.slug})


class GetCarGenetaionSlugView(View):
    def get(self, _, car_id) -> JsonResponse:
        try:
            car = CarGeneration.objects.get(pk=car_id)
        except:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Car with id: {car_id} does not exist",
                }
            )
        return JsonResponse({"error": False, "slug": car.slug})


class GetCarModificationSlugView(View):
    def get(self, _, car_id) -> JsonResponse:
        try:
            car = CarModification.objects.get(pk=car_id)
        except:
            return JsonResponse(
                {
                    "error": True,
                    "errorMessage": f"Car with id: {car_id} does not exist",
                }
            )
        return JsonResponse({"error": False, "slug": car.slug})
