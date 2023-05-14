from django.views.generic import TemplateView

from cars.models import Brand


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        brands = Brand.objects.all()
        context["brands"] = brands
        # context["brands_table"] = split_by_letter(brands)
        return context