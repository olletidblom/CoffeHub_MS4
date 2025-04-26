from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from allauth.account.models import EmailAddress
import stripe

from .models import Cart, CartItem, Order, OrderItem
from .forms import CheckoutForm
from products.models import Product


# ---------- CART VIEWS ---------- #
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f"'{product.name}' added to your cart.")
    return redirect('product_detail', pk=product_id)


@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    quantity_range = range(1, 11)
    return render(request, 'checkout/cart.html',
                  {'cart': cart, 'quantity_range': quantity_range})


@login_required
@require_POST
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        item.quantity = quantity
        item.save()
    return redirect('view_cart')


@login_required
@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    item.delete()
    return redirect('view_cart')


# ---------- CHECKOUT / STRIPE ---------- #
@login_required
def checkout(request):
    """
    1. Verify email is confirmed
    2. Collect address with CheckoutForm
    3. Create Stripe session
    """
    if not EmailAddress.objects.filter(user=request.user, verified=True).exists():
        messages.warning(request, "Please verify your email to proceed.")
        return redirect('view_cart')

    cart, _ = Cart.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            request.session["shipping_data"] = form.cleaned_data   # store temporarily
            return _stripe_session_redirect(request, cart)
    else:
        form = CheckoutForm()

    return render(request, "checkout/checkout.html", {"form": form})


def _stripe_session_redirect(request, cart):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    line_items = [{
        "price_data": {
            "currency": "usd",
            "product_data": {"name": item.product.name},
            "unit_amount": int(item.product.price * 100),
        },
        "quantity": item.quantity,
    } for item in cart.items.all()]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=request.build_absolute_uri('/checkout/success/'),
        cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        customer_email=request.user.email,
    )
    return redirect(session.url, code=303)


@login_required
def checkout_success(request):
    """Create Order, send email, clear cart."""
    shipping = request.session.pop("shipping_data", {})
    cart = Cart.objects.filter(user=request.user).first()

    if cart and cart.items.exists():
        order = Order.objects.create(user=request.user, **shipping)
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
        cart.items.all().delete()

        # confirmation email
        send_mail(
            subject='Your CoffeeHub Order Confirmation',
            message='Thanks for your order! We are processing it now.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
            fail_silently=False,
        )

    messages.success(request, "Thank you! Your order was successful.")
    return render(request, "checkout/checkout_success.html", {"order": order})


@login_required
def checkout_cancel(request):
    messages.warning(request, "Payment cancelled.")
    return render(request, "checkout/checkout_cancel.html")