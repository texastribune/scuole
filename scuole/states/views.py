# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from scuole.stats.models import SchoolYear

from .models import State, StateCohorts, StateStats


class StateDetailView(DetailView):
    model = State
    state_cohorts_model = StateCohorts

    def get_context_data(self, **kwargs):
        context = super(StateDetailView, self).get_context_data(**kwargs)
        state_cohorts = self.state_cohorts_model.objects.all()

        year = self.kwargs['state_year']

        if year:
            context['stat'] = get_object_or_404(
                StateStats, year__name=year, state=self.object)
        else:
            context['stat'] = get_object_or_404(
                StateStats, year=SchoolYear.objects.first(),
                state=self.object)

        context['latest_state_cohort'] = state_cohorts.latest_cohort

        return context
