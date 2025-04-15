from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('product_detail', pk=product_id)

def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'checkout/cart.html', {'cart': cart})