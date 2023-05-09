from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalogue.urls")),
    path("about/", include("about.urls")),
    path("cart/", include("cart.urls")),
    path("feedbacks/", include("feedbacks.urls")),
    path("contacts/", include("contacts.urls")),
    path("delivery-info/", include("payment_delivery.urls")),
    path("", include("cars.urls")),
    path("", include("spacers.urls")),
    path("", include("landing.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
