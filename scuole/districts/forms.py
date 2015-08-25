# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms

from .models import District


class DistrictAddForm(forms.ModelForm):
    class Meta:
        model = District
        fields = [
            'name',
            'tea_id',
            'street',
            'city',
            'state',
            'zip_code',
            'latitude',
            'longitude',
        ]
