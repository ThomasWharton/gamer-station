from django import template

"""
Custom filtering to ensure category heading
on products template does not appear if
no products visible within that category
"""
register = template.Library()

@register.filter
def filter_by_category(products, category):
    return [product for product in products if product.category == category]