from django.shortcuts import render

from store.models import Product

def store(request):
    products = Product.objects.all()
    products_count = products.count()

    return render(request, "store.html", context={"products": products,
                                                  "products_count": products_count,
                                                  })
