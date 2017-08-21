# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Campus, CampusStats
from scuole.districts.models import District, DistrictStats
from scuole.states.models import StateStats
from scuole.stats.models import SchoolYear
from scuole.counties.models import County


class CampusDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(
            Campus.objects.prefetch_related('principals'),
            slug=self.kwargs['slug'],
            district__slug=self.kwargs['district_slug'])

    def get_context_data(self, **kwargs):
        context = super(CampusDetailView, self).get_context_data(**kwargs)

        year = self.kwargs['campus_year']

        if year:
            context['stat'] = get_object_or_404(
                CampusStats, year__name=year, campus=self.object)
            context['district'] = get_object_or_404(
                DistrictStats, year__name=year, district=self.object.district)
            context['state'] = get_object_or_404(
                StateStats, year__name=year, state__name='TX')
        else:
            latest_year = SchoolYear.objects.first()

            context['stat'] = get_object_or_404(
                CampusStats, year=latest_year,
                campus=self.object)
            context['district'] = get_object_or_404(
                DistrictStats, year=latest_year, district=self.object.district)
            context['state'] = get_object_or_404(
                StateStats, year=latest_year, state__name='TX')

        context['county_cohorts'] = get_object_or_404(
            County, name=self.object.county)

        context['region_cohorts'] = get_object_or_404(
            District, name=self.object.district)

        return context
