# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import District, DistrictStats
from scuole.states.models import StateStats
from scuole.stats.models import SchoolYear


class DistrictListView(ListView):
    queryset = District.objects.all().defer('shape')


class DistrictDetailView(DetailView):
    queryset = District.objects.all().prefetch_related(
        'campuses')

    slug_url_kwarg = 'district_slug'

    def get_context_data(self, **kwargs):
        context = super(DistrictDetailView, self).get_context_data(**kwargs)

        year = self.kwargs['district_year']

        if year:
            context['stat'] = get_object_or_404(
                DistrictStats, year__name=year, district=self.object)
            context['state'] = get_object_or_404(
                StateStats, year__name=year, state__name='TX')
        else:
            latest_year = SchoolYear.objects.first()

            context['stat'] = get_object_or_404(
                DistrictStats, year=latest_year,
                district=self.object)
            context['state'] = get_object_or_404(
                StateStats, year=latest_year, state__name='TX')

        return context
