from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalogue.urls")),
    path("", include("cars.urls")),
    path("cart/", include("cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
