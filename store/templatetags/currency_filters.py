from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='currency')
def currency(value):
    """Format value as Indian Rupees"""
    try:
        return f"₹{float(value):,.2f}"
    except (ValueError, TypeError):
        return value
