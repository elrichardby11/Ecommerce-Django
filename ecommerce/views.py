from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all()[:9]

    return render(request, "index.html", context={"products": products})