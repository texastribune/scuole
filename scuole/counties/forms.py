# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms

from .models import County


class CountyAddForm(forms.ModelForm):
    class Meta:
        model = County
        fields = ['name', 'fips']
