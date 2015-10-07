# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView

from scuole.campuses.models import Campus
from scuole.districts.models import District


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        q = self.request.GET.get('q')

        context['matching_campuses'] = Campus.objects.filter(
            name__icontains=q).select_related('district')
        context['matching_districts'] = District.objects.filter(
            name__icontains=q).prefetch_related('campuses')

        return context
