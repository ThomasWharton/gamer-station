from django.shortcuts import render


def view_cart(request):
    """A view to see what is in customers cart"""

    return render(request, 'cart/cart.html')