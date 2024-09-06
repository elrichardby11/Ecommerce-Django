from carts.models import Cart, CartItem
from carts.views import cart_id


def counter_items(request):
    cart_count = 0

    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart)
        for cart_item in cart_items:
            cart_count += cart_item.quantity

    except Cart.DoesNotExist:
        cart_count = 0

    return {"cart_count": cart_count}