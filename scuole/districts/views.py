# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, ListView

from .models import District


class DistrictListView(ListView):
    queryset = District.objects.all().defer('shape')


class DistrictDetailView(DetailView):
    queryset = District.objects.all().prefetch_related(
        'campuses', 'stats__year')
    pk_url_kwarg = 'district_id'
    slug_url_kwarg = 'district_slug'
