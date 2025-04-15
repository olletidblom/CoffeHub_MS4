from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Cart, CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
        messages.success(request, f"'{product.name}' added to your cart.")
    else:
        messages.success(request, f"'{product.name}' added to your cart.")
    return redirect('product_detail', pk=product_id)

def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    quantity_range = range(1, 11)
    return render(request, 'checkout/cart.html', {'cart': cart, 'quantity_range': quantity_range})

@require_POST
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        item.quantity = quantity
        item.save()
        messages.success(request, f"Updated quantity for '{item.product.name}'.")
    return redirect('view_cart')

@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, f"Removed '{item.product.name}' from your cart.")
    return redirect('view_cart')