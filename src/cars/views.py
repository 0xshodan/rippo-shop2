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
        context = {"cars": brand.cars.all(), "url": "car"}
        return HttpResponse(template.render(context, request))


class CarsView(View):
    def get(self, request, slug):
        car = Car.objects.get(slug=slug)
        template = loader.get_template("cars.html")
        context = {"cars": car.generations.all(), "url": "generation"}
        return HttpResponse(template.render(context, request))


class GenerationView(View):
    def get(self, request, slug):
        car = CarGeneration.objects.get(slug=slug)
        template = loader.get_template("cars.html")
        context = {"cars": car.modifications.all(), "url": "modification"}
        return HttpResponse(template.render(context, request))


class ModificationView(View):
    def get(self, request, slug):
        car = CarModification.objects.get(slug=slug)
        template = loader.get_template("spacers.html")
        context = {"spacers": car.spacers.all()}
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
                    "name": generation.name,
                    "slug": generation.slug,
                }
            )
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
                    "name": modification.name,
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
