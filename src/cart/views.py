from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from cars.models import CarModification
from spacers.models import Spacer

from .cart import Cart


class CartView(View):
    def post(self, request):
        cart = Cart(request)
        spacer = Spacer.objects.get(pk=request.POST["id"])
        car = CarModification.objects.get(pk=request.POST["car_id"])
        cart.add(spacer, car, request.POST["type"])
        return HttpResponse()

    def get(self, request):
        return JsonResponse(Cart(request).cart)

    def delete(self, request, id, type):
        cart = Cart(request)
        spacer = Spacer.objects.get(pk=id)
        cart.remove(spacer, type=type)
        return HttpResponse()


# @require_POST
# def cart_add(request, spacer_id):
#     cart = Cart(request)
#     spacer = get_object_or_404(Spacer, pk=spacer_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(spacer=spacer, quantity=cd["quantity"], update_quantity=cd["update"])
#     return redirect("cart:cart_detail")


# def cart_remove(request, spacer_id):
#     cart = Cart(request)
#     product = get_object_or_404(Spacer, pk=spacer_id)
#     cart.remove(product)
#     return redirect("cart:cart_detail")


# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, "cart/detail.html", {"cart": cart})
