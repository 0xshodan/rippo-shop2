from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from cars.views import TestView

urlpatterns = [
    path("", TestView.as_view()),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalogue.urls")),
    path("", include("cars.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
