from django import template

register = template.Library()

@register.filter
def filter_by_category(products, category):
    return [product for product in products if product.category == category]