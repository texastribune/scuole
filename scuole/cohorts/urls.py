# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import path

from .views import (
    AcceptCohortRedirectView,
    CohortsLandingView,
    CountyCohortsDetailView,
    RegionCohortsDetailView,
    StateCohortsDetailView,
)

app_name = "cohorts"

urlpatterns = [
    path("", CohortsLandingView.as_view(), name="landing"),
    path("states/<slug:slug>/", StateCohortsDetailView.as_view(), name="states"),
    path("regions/<slug:slug>/", RegionCohortsDetailView.as_view(), name="regions"),
    path("counties/<slug:slug>/", CountyCohortsDetailView.as_view(), name="counties"),
    path("redirect/", AcceptCohortRedirectView.as_view(), name="redirect"),
]
