from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from spacers.models import Spacer

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, spacer_id):
    cart = Cart(request)
    spacer = get_object_or_404(Spacer, pk=spacer_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(spacer=spacer, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("cart:cart_detail")


def cart_remove(request, spacer_id):
    cart = Cart(request)
    product = get_object_or_404(Spacer, pk=spacer_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})
