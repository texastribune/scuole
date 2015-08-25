# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms

from .models import Region


class RegionAddForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'region_id']
