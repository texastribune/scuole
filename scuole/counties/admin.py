# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from scuole.core.admin import ReadOnlyAdmin
from .models import County, CountyCohorts


@admin.register(County)
class CountyAdmin(ReadOnlyAdmin):
    search_fields = ['name']


@admin.register(CountyCohorts)
class CountyCohortsAdmin(ReadOnlyAdmin):
    list_filter = (
        'year__name', 'county__name', 'gender', 'ethnicity', 'economic_status',)
    search_fields = ('county__name',)
