from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from carts.models import CartItem
from carts.views import cart_id
from category.models import Category
from store.models import Product

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all()
    
    products_count = products.count()
    paged_products = pagination(request, products, 3)

    return render(request, "store.html", context={
        "category": categories,
        "products": paged_products,
        "products_count": products_count,
    })

def pagination(request, products, products_by_page):
    paginator = Paginator(products, products_by_page)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)
    
    return paged_products

def product_detail(request, category_slug, product_slug):
    count=0
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=cart_id(request), product=product).exists()

    if in_cart:
        count = CartItem.objects.get(cart__cart_id=cart_id(request), product=product).quantity

    context = {
        "product": product,
        "in_cart": in_cart,
        "count": count,
    }

    return render(request, "product_detail.html", context)
