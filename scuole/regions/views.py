# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from scuole.cohort.models import CohortYear
from scuole.states.models import StateStats

from .models import County, CountyCohorts


class CountyListView(ListView):
    queryset = County.objects.all().defer('shape')


class CountyDetailView(DetailView):
    queryset = County.objects.all()

    slug_url_kwarg = 'county_slug'

    def get_context_data(self, **kwargs):
        context = super(CountyDetailView, self).get_context_data(**kwargs)

        year = CohortYear.objects.first()

        context['state'] = get_object_or_404(
            StateStats, year__name=year, state__name='TX')

        context['cohort'] = get_object_or_404(
            CountyCohorts, year__name=year, county=self.object)

        return context


# Create your views here.
