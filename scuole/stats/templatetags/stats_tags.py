# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat
import six
from django.utils.html import format_html

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
       if isinstance(value, int) or value.is_integer():
           # For integers, format without decimal places
           return (intcomma(int(value)), '')
       else:
           # For decimals, apply floatformat first then intcomma
           formatted = floatformat(value)
           return (intcomma(float(formatted)), '')

    return value


@register.simple_tag
def display_stat(stat, key, value_type=None, value_label=False):
    value = get_by_key(stat, key)

    if callable(value):
        value = value()

    display_value, display_descriptor = get_value_display(value, value_type)

    if value_label and display_descriptor != '$':
        html = format_html(
            '<span class="metric-value-label"> {}</span>', display_descriptor)
        display_descriptor = html

    if display_descriptor == '$':
        output = format_html('{}{}', display_descriptor, display_value)
    elif display_descriptor == 'years':
        output = format_html('{} {}', display_value, display_descriptor)
    else:
        output = format_html('{}{}', display_value, display_descriptor)

    return output

@register.simple_tag
def accountability_year_stat(stat, key):
    value = get_by_key(stat, key)
    return value
