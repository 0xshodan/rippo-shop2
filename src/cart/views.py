from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View

from cars.models import CarModification
from spacers.models import Spacer

from .cart import Cart


class CartView(View):
    def post(self, request):
        cart = Cart(request)
        spacer = Spacer.objects.get(pk=request.POST["id"])
        car = CarModification.objects.get(pk=request.POST["car_id"])
        data = cart.add(spacer, car, request.POST["type"])
        return JsonResponse(data)

    def get(self, request):
        return JsonResponse(Cart(request).cart)

    def delete(self, request):
        cart = Cart(request)
        data = QueryDict(request.body)
        cart.remove(spacer_id=data["id"])
        return HttpResponse()

    def patch(self, request):
        cart = Cart(request)
        data = QueryDict(request.body)
        if data["quantity"] == "1":
            cart.increment_quantity(data["id"])
        elif data["quantity"] == "-1":
            cart.decrement_quantity(data["id"])
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
