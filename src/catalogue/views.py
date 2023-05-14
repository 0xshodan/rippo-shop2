from django.views.generic.base import TemplateView

from cars.models import Brand


def split_by_letter(lst: list[Brand]) -> list[list[Brand]]:
    current_letter = None
    current_list = []
    ret = []
    for i in lst:
        if current_letter is None:
            current_letter = i.name[0]
            current_list.append(i)
        else:
            if current_letter == i.name[0]:
                current_list.append(i)
            else:
                current_letter = i.name[0]
                ret.append(current_list)
                current_list = []
                current_list.append(i)
    ret.append(current_list)
    return ret


class CatalogueView(TemplateView):
    template_name = "pages/catalogue.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CatalogueView, self).get_context_data(*args, **kwargs)
        brands = Brand.objects.all()
        context["brands"] = brands
        # context["brands_table"] = split_by_letter(brands)
        return context
