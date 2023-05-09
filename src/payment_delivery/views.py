from django.views.generic import TemplateView


class PaymentDeliveryView(TemplateView):
    template_name = "payment_delivery.html"
