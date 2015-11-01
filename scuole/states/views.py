# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import State, StateStats
from scuole.stats.models import SchoolYear


class StateDetailView(DetailView):
    model = State

    def get_context_data(self, **kwargs):
        context = super(StateDetailView, self).get_context_data(**kwargs)

        year = self.kwargs['state_year']

        if year:
            context['stat'] = get_object_or_404(
                StateStats, year__name=year, state=self.object)
        else:
            context['stat'] = get_object_or_404(
                StateStats, year=SchoolYear.objects.first(),
                state=self.object)

        return context
