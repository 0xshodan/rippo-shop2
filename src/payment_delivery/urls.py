from django.urls import path

from .views import PaymentDeliveryView

urlpatterns = [path("", PaymentDeliveryView.as_view())]
