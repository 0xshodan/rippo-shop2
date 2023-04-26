from django.urls import path

from .views import CatalogueView

urlpatterns = [
    path("", CatalogueView.as_view(), name="catalogue"),
]
