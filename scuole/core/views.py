# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from operator import itemgetter

from django.http import JsonResponse
from django.views.generic import TemplateView, View

from scuole.campuses.models import Campus
from scuole.districts.models import District


class AboutView(TemplateView):
    template_name = 'about.html'


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


class LookupView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        q = self.request.GET.get('q')

        campuses = [
            {'name': i.name,
             'url': i.get_absolute_url(),
             'type': 'Campus - {}'.format(i.district.name)}
            for i in Campus.objects.filter(
                name__icontains=q).select_related('district__name')[:15]]

        districts = [
            {'name': i.name, 'url': i.get_absolute_url(), 'type': 'District'}
            for i in District.objects.filter(
                name__icontains=q)[:15]]

        context['results'] = sorted(
            campuses + districts, key=itemgetter('name'))

        return JsonResponse(context, **kwargs)


class LandingView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        context['district_count'] = District.objects.count()
        context['campus_count'] = Campus.objects.count()

        return context
