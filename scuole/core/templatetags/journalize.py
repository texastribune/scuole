from django import template

register = template.Library()


@register.filter
def percentify(value):
    if value <= 1:
        value = value * 100

    return '{:.1f}'.format(value)
