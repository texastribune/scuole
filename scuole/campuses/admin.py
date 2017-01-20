# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from scuole.core.admin import ReadOnlyAdmin
from .models import Campus, CampusStats


@admin.register(Campus)
class CampusAdmin(ReadOnlyAdmin):
    search_fields = ('name', 'tea_id')


@admin.register(CampusStats)
class CampusStatsAdmin(ReadOnlyAdmin):
    list_filter = ('year__name',)
    search_fields = ('campus__name', 'campus__tea_id')
