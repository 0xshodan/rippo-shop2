from django.urls import path

from .views import (
    BrandsView,
    CarApiView,
    CarGenerationApiView,
    CarModificationApiView,
    CarsView,
    GenerationView,
    GetBrandSlugView,
    GetCarGenetaionSlugView,
    GetCarModificationSlugView,
    GetCarSlugView,
    ModificationView,
)

urlpatterns = [
    path("api/cars/<brand_id>", CarApiView.as_view(), name="cars"),
    path(
        "api/generations/<car_id>",
        CarGenerationApiView.as_view(),
        name="car_generations",
    ),
    path(
        "api/modifications/<car_id>",
        CarModificationApiView.as_view(),
        name="car_modifications",
    ),
    path("api/slugs/brand/<int:brand_id>", GetBrandSlugView.as_view()),
    path("api/slugs/car/<int:car_id>", GetCarSlugView.as_view()),
    path("api/slugs/cargen/<int:car_id>", GetCarGenetaionSlugView.as_view()),
    path("api/slugs/carmod/<int:car_id>", GetCarModificationSlugView.as_view()),
    path("brand/<slug:slug>/", BrandsView.as_view(), name="cars_page"),
    path("car/<slug:slug>/", CarsView.as_view(), name="generations_page"),
    path(
        "generation/<slug:slug>/", GenerationView.as_view(), name="modifications_page"
    ),
    path("modification/<slug:slug>/", ModificationView.as_view(), name="spacers_page"),
]
