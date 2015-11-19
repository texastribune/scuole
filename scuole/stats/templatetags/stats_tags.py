# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat

register = template.Library()


@register.filter
def absolute(value):
    return abs(value)


@register.filter
def subtract(value, other):
    return value - other


@register.filter
def get_by_key(value, key):
    return getattr(value, key, None)


@register.filter
def display_value(value, value_type=None):
    if not value:
        return 'N/A'

    if value < 0:
        return 'Masked'

    if value_type == 'dollars':
        return intcomma(floatformat(value, "0"))

    if value_type in ('percent', 'years'):
        return floatformat(value)

    if value_type == 'test_score':
        return value

    if value_type == 'number':
        return intcomma(floatformat(value))

    return value
