# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from scuole.core.admin import ReadOnlyAdmin
from .models import District


@admin.register(District)
class DistrictAdmin(ReadOnlyAdmin):
    pass
