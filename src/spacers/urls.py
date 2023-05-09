from django.urls import path

from .views import update_price

urlpatterns = [path("update_price/", update_price)]
