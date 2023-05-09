from django.http import HttpResponseRedirect

from .models import Spacer


def update_price(request):
    if request.POST:
        percent = int((request.POST)["percent"])
        spacers = list(Spacer.objects.all())
        for i, spacer in enumerate(spacers):
            spacer.price20mm = spacer.price20mm + int(spacer.price20mm / 100 * percent)
            spacer.price30mm = spacer.price30mm + int(spacer.price30mm / 100 * percent)
            spacer.price40mm = spacer.price40mm + int(spacer.price40mm / 100 * percent)
            spacer.price50mm = spacer.price50mm + int(spacer.price50mm / 100 * percent)
            spacers[i] = spacer
        Spacer.objects.bulk_update(spacers, ["price20mm","price30mm","price40mm","price50mm"])
        return HttpResponseRedirect("/admin/spacers/spacer/")