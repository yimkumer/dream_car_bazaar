# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def split(value):
    return value.split(' ')
