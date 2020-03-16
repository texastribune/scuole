# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from operator import itemgetter

from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from scuole.campuses.models import Campus
from scuole.districts.models import District
from scuole.stats.models import SchoolYear

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        latest_year = SchoolYear.objects.first()
        end_year = SchoolYear.objects.first().end_year

        context['latest_year'] = latest_year
        context['end_year'] = end_year

        return context


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        if not self.request.GET.get('q'):
            return redirect('landing')

        return super(SearchView, self).get(request, *args, **kwargs)

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
                name__icontains=q).select_related('district')[:15]]

        districts = [
            {'name': i.name, 'url': i.get_absolute_url(), 'type': 'District'}
            for i in District.objects.filter(
                name__icontains=q)[:15]]

        context['results'] = sorted(
            campuses + districts, key=itemgetter('name'))

        return JsonResponse(context, **kwargs)


class LandingView(TemplateView):
    """
    The view for the landing page. Pulls in counts for `District` and `Campus`.
    """

    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        context['district_count'] = District.objects.count()
        context['campus_count'] = Campus.objects.count()

        return context


class AcceptRedirectView(View):
    """
    The `AcceptRedirectView` is intended to be the recipient of redirected
    visitors from the previous version of public schools in the texastribune
    app. It attempts to parse the URL of the page sent its way and guide the
    user to the campus or district they wanted, if possible. Otherwise, they go
    to the home page.
    """

    def get(self, request, *args, **kwargs):
        request_params = request.GET

        district_slug = request_params.get('district_slug')
        campus_slug = request_params.get('campus_slug')

        if campus_slug and district_slug:
            try:
                return redirect(Campus.objects.get(
                    district__slug=district_slug, slug=campus_slug))
            except Campus.DoesNotExist:
                pass

        if district_slug:
            try:
                return redirect(District.objects.get(slug=district_slug))
            except District.DoesNotExist:
                pass

        return redirect('landing')
