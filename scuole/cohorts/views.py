# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from json import dumps

# from django.shortcuts import get_list_or_404
from django.views.generic import TemplateView, DetailView

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
        context['latest_state_cohort'] = StateCohorts.objects.latest_cohort(
            state__name='TX')

        data = cohorts.select_related('year').data_payload()
        context['data'] = data
        context['js_data'] = dumps(data)

        context['county_list'] = County.objects.all().defer('shape')
        context['region_list'] = Region.objects.all().defer('shape')

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
        context['latest_state_cohort'] = StateCohorts.objects.latest_cohort(
            state__name='TX')

        data = cohorts.select_related('year').data_payload()
        context['data'] = data
        context['js_data'] = dumps(data)

        context['county_list'] = County.objects.all().defer('shape')
        context['region_list'] = Region.objects.all().defer('shape')

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

        data = cohorts.select_related('year').data_payload()
        context['data'] = data
        context['js_data'] = dumps(data)

        context['county_list'] = County.objects.all().defer('shape')
        context['region_list'] = Region.objects.all().defer('shape')

        return context


class CohortsLandingView(TemplateView):
    model = County
    region_model = Region
    template_name = 'cohorts_landing.html'

    def get_context_data(self, **kwargs):
        context = super(
            CohortsLandingView, self).get_context_data(**kwargs)

        context['county_list'] = self.model.objects.all().defer('shape')
        context['region_list'] = self.region_model.objects.all().defer('shape')

        return context
