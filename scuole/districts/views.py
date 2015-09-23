# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, ListView

from .models import District, DistrictStats


class DistrictListView(ListView):
    model = District


class DistrictDetailView(DetailView):
    model = District
    pk_url_kwarg = 'district_id'
    slug_url_kwarg = 'district_slug'
