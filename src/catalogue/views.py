from django.views.generic.base import TemplateView


class CatalogueView(TemplateView):
    template_name = "pages/catalogue.html"
