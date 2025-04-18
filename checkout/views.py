from django.shortcuts import render, redirect, get_object_or_404
from allauth.account.models import EmailAddress
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Cart, CartItem
from products.models import Product
import stripe
from django.conf import settings
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    quantity_range = range(1, 11)
    return render(request, 'checkout/cart.html', {'cart': cart, 'quantity_range': quantity_range})

@login_required
@require_POST
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        item.quantity = quantity
        item.save()
        messages.success(request, f"Updated quantity for '{item.product.name}'.")
    return redirect('view_cart')

@login_required
@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, f"Removed '{item.product.name}' from your cart.")
    return redirect('view_cart')



@login_required
def checkout(request):
    if not EmailAddress.objects.filter(user=request.user, verified=True).exists():
        messages.warning(request, "Please verify your email address to proceed to checkout.")
        return redirect('view_cart')
    if not settings.STRIPE_SECRET_KEY:
        messages.error(request, "Payment service is not configured.")
        return redirect('view_cart')
    
    cart, _ = Cart.objects.get_or_create(user=request.user)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    line_items = []
    for item in cart.items.all():
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100),
            },
            'quantity': item.quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/checkout/success/'),
        cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        customer_email=request.user.email,
    )

    return redirect(session.url, code=303)


def checkout_success(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart.items.all().delete()
    messages.success(request, "Thank you! Your order has been placed successfully.")
    return render(request, 'checkout/checkout_success.html')

def checkout_cancel(request):
    messages.warning(request, "Your payment was canceled.")
    return render(request, 'checkout/checkout_cancel.html')