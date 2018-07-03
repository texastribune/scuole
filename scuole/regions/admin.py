# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from scuole.core.admin import ReadOnlyAdmin

from .models import Region, RegionCohorts, RegionStats


@admin.register(Region)
class RegionAdmin(ReadOnlyAdmin):
    search_fields = ['name']


@admin.register(RegionStats)
class RegionStatsAdmin(ReadOnlyAdmin):
    list_filter = ('year__name',)
    search_fields = ('region__name',)


@admin.register(RegionCohorts)
class RegionCohortsAdmin(ReadOnlyAdmin):
    list_filter = (
        'year__name', 'region__name', 'gender', 'ethnicity', 'economic_status',)
    search_fields = ('region__name',)
