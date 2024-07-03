from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """A view to show an individual products details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, 'products/product_detail.html', context)
