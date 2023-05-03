from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from cars.views import TestView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalogue.urls")),
    path("", include("cars.urls")),
    path("", TestView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
