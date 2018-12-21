# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from json import dumps

from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView, View

from scuole.core.utils import build_geojson
from scuole.counties.models import County, CountyCohorts
from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts
from scuole.stats.models import SchoolYear

distinct_cohort_counties = (
    County.objects.filter(cohorts__in=CountyCohorts.objects.all())
    .distinct()
    .defer("shape")
    .order_by("name")
)


class CountyCohortsDetailView(DetailView):
    model = County
    cohorts_model = CountyCohorts
    template_name = "cohorts/county_cohorts_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CountyCohortsDetailView, self).get_context_data(**kwargs)

        cohorts = self.cohorts_model.objects.filter(county=self.object)
        latest_cohort_year = SchoolYear.objects.get(name="2006-2007")

        context["latest_cohort"] = cohorts.latest_cohort(county=self.object)
        context["latest_state_cohort"] = StateCohorts.objects.latest_cohort(
            state__name="TX"
        )

        cohorts = cohorts.select_related("year")
        data = cohorts.data_payload()
        context["data"] = data
        context["latest_data"] = cohorts.data_payload(latest_cohort_year)
        context["js_data"] = dumps(data)

        context["county_list"] = distinct_cohort_counties
        context["region_list"] = Region.objects.all().defer("shape")

        return context


class RegionCohortsDetailView(DetailView):
    model = Region
    cohorts_model = RegionCohorts
    template_name = "cohorts/region_cohorts_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RegionCohortsDetailView, self).get_context_data(**kwargs)

        cohorts = self.cohorts_model.objects.filter(region=self.object)
        latest_cohort_year = SchoolYear.objects.get(name="2006-2007")

        context["latest_cohort"] = cohorts.latest_cohort(region=self.object)
        context["latest_state_cohort"] = StateCohorts.objects.latest_cohort(
            state__name="TX"
        )

        cohorts = cohorts.select_related("year")
        data = cohorts.data_payload()
        context["data"] = data
        context["latest_data"] = cohorts.data_payload(latest_cohort_year)
        context["js_data"] = dumps(data)

        context["county_list"] = distinct_cohort_counties
        context["region_list"] = Region.objects.all().defer("shape")

        return context


class StateCohortsDetailView(DetailView):
    model = State
    cohorts_model = StateCohorts
    template_name = "cohorts/state_cohorts_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StateCohortsDetailView, self).get_context_data(**kwargs)

        cohorts = self.cohorts_model.objects.filter(state=self.object)
        latest_cohort_year = SchoolYear.objects.get(name="2006-2007")

        context["latest_cohort"] = cohorts.latest_cohort(state=self.object)

        cohorts = cohorts.select_related("year")
        data = cohorts.data_payload()
        context["data"] = data
        context["latest_data"] = cohorts.data_payload(latest_cohort_year)
        context["js_data"] = dumps(data)

        context["county_list"] = distinct_cohort_counties
        context["region_list"] = Region.objects.all().defer("shape")

        return context


class CohortsLandingView(TemplateView):
    model = County
    region_model = Region
    template_name = "cohorts_landing.html"

    def get_context_data(self, **kwargs):
        context = super(CohortsLandingView, self).get_context_data(**kwargs)

        context["county_list"] = distinct_cohort_counties
        context["region_list"] = self.region_model.objects.all().defer("shape")

        context["regions_geojson"] = build_geojson(
            Region.objects.all(), "shape", ["region_name_with_city"]
        )

        return context


class AcceptCohortRedirectView(View):
    """
    The `AcceptCohortRedirectView` is intended to be the recipient of redirected
    visitors from the previous version of cohorts in the texastribune app. It
    attempts to parse the URL of the page sent its way and guide the user to
    the region or county they wanted, if possible. Otherwise, they go to the
    home page.
    """

    def get(self, request, *args, **kwargs):
        request_params = request.GET

        region_slug = request_params.get("region_slug")
        county_slug = request_params.get("county_slug")

        if region_slug:
            region_name = region_slug.replace("-", " ").title()

            try:
                return redirect(
                    "cohorts:regions", slug=Region.objects.get(name=region_name).slug
                )
            except Region.DoesNotExist:
                pass

        if county_slug:
            county_slug = "el-paso" if county_slug == "el-pasohudspeth" else county_slug
            try:
                return redirect(
                    "cohorts:counties", slug=County.objects.get(slug=county_slug).slug
                )
            except County.DoesNotExist:
                pass

        return redirect("cohorts:landing")
