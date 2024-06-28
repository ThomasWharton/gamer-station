from django.shortcuts import render
from .models import Product, Category



def all_products(request):
    """A view to show all products including sorting and search queries"""

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)
