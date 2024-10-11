from django.shortcuts import render
from bangazonapi.models import Product

def expensive_products_report(request):
    expensive_products = Product.objects.filter(price__gt=1000)
    return render(request, 'reports/expensive_products.html', {'products': expensive_products})

