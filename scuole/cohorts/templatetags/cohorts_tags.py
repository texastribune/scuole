# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template

register = template.Library()


@register.filter
def maskNA(value):
    if value is None:
        return 'N/A'
    else:
        return value
