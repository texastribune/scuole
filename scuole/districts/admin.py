# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from scuole.core.admin import ReadOnlyAdmin

from .models import District, DistrictStats


@admin.register(District)
class DistrictAdmin(ReadOnlyAdmin):
    search_fields = ('name', 'tea_id')


@admin.register(DistrictStats)
class DistrictStatsAdmin(ReadOnlyAdmin):
    list_filter = ('year__name',)
    search_fields = ('district__name',)
