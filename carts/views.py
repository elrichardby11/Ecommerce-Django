from django.shortcuts import redirect, render

from carts.models import Cart, CartItem
from store.models import Product

def cart_id(request):
    cart = request.session.session_key
    print("cart", cart)
    if cart is None:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect("cart")

def remove_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")

def remove_cart_item(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()

    return redirect("cart")
    
def cart(request, total=0, quantity=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = None
        cart_items = []
    else:
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            cart_item.subtotal = cart_item.quantity * cart_item.product.price
            total += (cart_item.quantity * cart_item.product.price)
            quantity += cart_item.quantity

    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "IVA": (total * 0.19),
    }

    return render(request, "cart.html", context=context)
