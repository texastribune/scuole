# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import include, re_path

from scuole.campuses.views import CampusDetailView

from . import views

app_name = "districts"

urlpatterns = [
    re_path(r"^$", views.DistrictListView.as_view(), name="list"),
    re_path(
        r"^(?P<district_slug>[\w-]+)/(?:(?P<district_year>[0-9]{4}-[0-9]{4})/)?",
        include(
            [
                re_path(r"^$", views.DistrictDetailView.as_view(), name="detail"),
                re_path(
                    r"^(?P<slug>[\w-]+)/(?:(?P<campus_year>[0-9]{4}-[0-9]{4})/)?$",
                    CampusDetailView.as_view(),
                    name="campus",
                ),
            ]
        ),
    ),
]

# Experiment with reworking paths
# urlpatterns = [
#     path("", views.DistrictListView.as_view(), name="list"),
#     path("<district_slug>/", views.DistrictDetailView.as_view(), name="detail"),
#     path(
#         "<district_slug>/<district_year>/",
#         views.DistrictDetailView.as_view(),
#         name="detail",
#     ),
# ]
