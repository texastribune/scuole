# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from scuole.districts.models import District

from .models import Campus


class CampusDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(
            Campus.objects.prefetch_related('principals'),
            slug=self.kwargs['slug'], district__pk=self.kwargs['district_id'])
