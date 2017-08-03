# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from scuole.core.admin import ReadOnlyAdmin
from .models import State, StateStats, StateCohorts


@admin.register(State)
class StateAdmin(ReadOnlyAdmin):
    pass


@admin.register(StateStats)
class StateStatsAdmin(ReadOnlyAdmin):
    pass


@admin.register(StateCohorts)
class StateCohortsAdmin(ReadOnlyAdmin):
    search_fields = ('state__name',)
