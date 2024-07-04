from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Avg, Count, Q
from .models import Product, Category




def all_products(request):
    """A view to show all products including sorting and search queries"""

    products = Product.objects.annotate(
        average_rating=Avg('reviews__rating'),
        review_count=Count('reviews'),
    )
    categories = Category.objects.all()
    query = None
    category = None
    sub_category = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
        
        if 'sub_category' in request.GET:
            sub_category = request.GET['sub_category']
            products = products.filter(sub_category=sub_category)

    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
        'selected_category': category,
        'selected_sub_category': sub_category,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show an individual products details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
        'average_rating': product.average_rating(),
    }

    return render(request, 'products/product_detail.html', context)
