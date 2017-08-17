# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from json import dumps

# from django.shortcuts import get_list_or_404
from django.views.generic import DetailView

from scuole.counties.models import County, CountyCohorts
from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts


class CountyCohortsDetailView(DetailView):
    model = County
    cohorts_model = CountyCohorts
    template_name = 'cohorts/county_cohorts_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            CountyCohortsDetailView, self).get_context_data(**kwargs)

        cohorts = self.cohorts_model.objects.filter(county=self.object)

        context['latest_cohort'] = cohorts.latest_cohort(
            county=self.object)
        context['js_data'] = dumps(cohorts.select_related('year').data_payload())

        return context


class RegionCohortsDetailView(DetailView):
    model = Region
    cohorts_model = RegionCohorts
    template_name = 'cohorts/region_cohorts_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            RegionCohortsDetailView, self).get_context_data(**kwargs)

        cohorts = self.cohorts_model.objects.filter(region=self.object)

        context['latest_cohort'] = cohorts.latest_cohort(
            region=self.object)
        context['js_data'] = dumps(cohorts.select_related('year').data_payload())

        return context


class StateCohortsDetailView(DetailView):
    model = State
    cohorts_model = StateCohorts
    template_name = 'cohorts/state_cohorts_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            StateCohortsDetailView, self).get_context_data(**kwargs)

        cohorts = self.cohorts_model.objects.filter(state=self.object)

        context['latest_cohort'] = cohorts.latest_cohort(
            state=self.object)
        context['js_data'] = dumps(cohorts.select_related('year').data_payload())

        return context
