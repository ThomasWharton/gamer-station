from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from .models import Product, Category
from .forms import ProductForm



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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Naughty boy!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Well done, you successfully added a product! Way to go big man!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. You done messed up big man!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Naughty boy!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Well done, you successfully updated a product! Way to go big man!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. You done messed up big man!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Naughty boy!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product')
    return redirect (reverse('products'))
