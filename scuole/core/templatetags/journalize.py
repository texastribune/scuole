from django import template

register = template.Library()


@register.filter
def percentify(value):
    try:
        if value <= 1:
            value = value * 100
    except TypeError:
        return None

    return '{:.1f}'.format(value)
