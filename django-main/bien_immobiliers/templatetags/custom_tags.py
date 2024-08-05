from django import template

register = template.Library()

@register.filter(name='capitalize')
def capitalize_filter(value):
    return value.title()