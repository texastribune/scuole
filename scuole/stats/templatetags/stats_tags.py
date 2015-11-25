# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat
from django.utils import six

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
def get_value_display(value, value_type):
    if value is None:
        return ('N/A', '')

    if isinstance(value, six.string_types):
        return (value, '')

    if value < 0:
        return ('Masked', '')

    if value_type == 'dollars':
        return (intcomma(floatformat(value, "0")), '$')

    if value_type == 'percent':
        return (floatformat(value), '%')

    if value_type == 'years':
        return (floatformat(value), 'years')

    if value_type == 'test_score':
        return (value, '')

    if value_type == 'number':
        return (intcomma(floatformat(value)), '')

    return value


@register.simple_tag
def display_stat(stat, key, value_type=None, value_label=False):
    value = get_by_key(stat, key)

    if callable(value):
        value = value()

    display_value, display_descriptor = get_value_display(value, value_type)

    if value_label and display_descriptor != '$':
        html = '<span class="metric-value-label"> {}</span>'.format(
            display_descriptor)
        display_descriptor = html

    if display_descriptor == '$':
        output = '{}{}'.format(display_descriptor, display_value)
    elif display_descriptor == 'years':
        output = '{} {}'.format(display_value, display_descriptor)
    else:
        output = '{}{}'.format(display_value, display_descriptor)

    return output
